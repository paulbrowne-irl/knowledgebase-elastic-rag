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

def walk_directory_ingest_files(starting_dir,es_index):
    '''
    Do recursive walk of all files and folders in directior
    '''
    logging.debug("directory:"+starting_dir)
    logging.debug("Will ingest to elastic index:"+es_index)

    # read config once
    do_pdf_ocr= config.read_boolean("READ_PDF_USING_OCR")
    es_index_name= config.read("ES_INDEX_KB")

    #########
    # iterate over files in directory
    # including sub directories
    #########
    for filename in os.listdir(starting_dir):

        #reset document text
        document_text=""

        try:

            # Get the next file in this directory
            full_filepath = os.path.join(starting_dir, filename)

            #########
            # Check if this is a sub directory
            #########
            if(os.path.isdir(full_filepath)):
                logging.info("Recursive call to handle directory:"+full_filepath)
                walk_directory_ingest_files(full_filepath,es_index)

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
            logging.info("No text extracted to add to KB")
        else:
            logging.info("Indexing text in KB")
            index_elastic.index(es_index_name,full_filepath,document_text)
        
        



# simple code to run from command line
if __name__ == '__main__':

    #Set the Logging level. Change it to logging.INFO is you want just the important info
    #logging.basicConfig(filename=config.read("LOG_FILE"), encoding='utf-8', level=logging.DEBUG)
    logging.basicConfig(level=logging.DEBUG)


    # get config
    starting_dir = config.read("SOURCE_DIR_FILES")
    es_index=config.read("ES_INDEX_KB")
   

    #call the main method in this module
    walk_directory_ingest_files(starting_dir, es_index)