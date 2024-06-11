import logging
import os

import settings.config as config

import util.extract.extract_email as extract_email
import util.extract.extract_pdf as extract_pdf
import util.extract.extract_word as extract_word
import util.index.index_elastic as index_elastic


'''
Simple gateway to the ingestion app
'''

def walk_directories_ingest_files(starting_dir_list:list,es_index:str):
    '''
    Do recursive walk of all files and folders in directory
    '''
    logging.info("list of directories to index:"+str(starting_dir_list))
    logging.info("Will ingest to elastic index:"+es_index)

    # read config once
    do_pdf_ocr= config.read_boolean("READ_PDF_USING_OCR")
    es_index_name= config.read("ES_INDEX_KB")

    #########
    # iterate over multiple directories
    #########
    for single_dir in starting_dir_list:

        #########
        # iterate over files in directory
        # including sub directories
        #########
        for filename in os.listdir(single_dir):

            #reset document text
            document_text=""

            try:

                # Get the next file in this directory
                full_filepath = os.path.join(single_dir, filename)

                #########
                # Check if this is a sub directory
                #########
                if(os.path.isdir(full_filepath)):
                    logging.info("Recursive call to handle directory:"+full_filepath)
                    #package as list
                    full_filepath_as_list=[full_filepath]
                    walk_directories_ingest_files(full_filepath_as_list,es_index)

                #########
                # pdf
                #########
                elif filename.lower().endswith(".pdf"):

                    logging.info("processing pdf file: "+filename)

                    # Extract information using two methodologies
                    document_text = extract_pdf.extract_text_info_no_ocr(full_filepath)

                    if(do_pdf_ocr):
                        document_text= document_text+extract_pdf.extract_text_info_with_ocr(full_filepath)

                    #logging.info("Extracted Text:"+document_text)

                #########
                # Word
                #########
                elif filename.lower().endswith(".docx"):
                    logging.info("processing word file: "+filename)

                    # Extract _extract_text_stats information
                    document_text = extract_word.loop_extract_text_info_word(full_filepath)
                    
            #########
                # Outlook MSG
                #########

                elif filename.lower().endswith(".msg"):
                    logging.info("processing email format: "+filename)
                    document_text = extract_email.extract_text_email(full_filepath)
            
                #########
                # Excel
                #########

                elif filename.lower().endswith(".xlsx"):
                    logging.info("skipping excel file: "+filename)

    
                #########
                # Other files
                #########

                else:
                    logging.info("Ignoring unknown format  format: "+filename)


            except Exception as problem:

                # decide how to handle it
                if config.read_boolean("CONTIUE_LOOP_AFTER_ERROR"):
                    # Log the error and continue loop
                    logging.error(problem)

                else:
                    # rethrow the error and end
                    raise problem
            

            # add to index if we have text
            if(document_text==""):
                logging.info("No text extracted to index")
            else:
                logging.info("Indexing extracted text into Index")
                index_elastic.index(es_index_name,full_filepath,document_text)
            
        



# simple code to run from command line
if __name__ == '__main__':

    #Set the Logging level. Change it to logging.INFO is you want just the important info
    #logging.basicConfig(filename=config.read("LOG_FILE"), encoding='utf-8', level=logging.DEBUG)
    logging.basicConfig(level=logging.INFO)


    # get config
    starting_point_dict = config.read_dict("SOURCE_DIRECTORIES")
    starting_dir_list = [*starting_point_dict.values()]

    es_index=config.read("ES_INDEX_KB")
   

    #call the main method in this module
    walk_directories_ingest_files(starting_dir_list, es_index)