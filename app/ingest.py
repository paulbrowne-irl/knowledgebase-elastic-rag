import logging
import os

import settings.config as config
import util.index.extract_email as extract_email
import util.index.extract_pdf as extract_pdf
import util.index.extract_word as extract_word

import util.index.index_elastic as index_elastic

# KEYS FOR STORING METADATA IN DICT
DATA_SOURCE= "DATA_SOURCE"
FILE_NAME ="FILE_NAME"
PARENT_FOLDER="PARENT_FOLDER"

# read config once
do_pdf_ocr= config.read_boolean("READ_PDF_USING_OCR")
es_index_name= config.read("ES_INDEX_KB")




def _extract_metadata(configsource: str, fullfilepath: str) -> dict:
    ''' generate a dictionary of metadat based on the information passed in
    * current file name
    * parent folder name
    * the generic bucket that the config file came from
    '''
    meta_data= {}

    # add values to it
    meta_data[DATA_SOURCE]=configsource

    #split fullfilepath
    rest_path, file = os.path.split(fullfilepath)
    meta_data[FILE_NAME]= file

    parent_folder= rest_path.rpartition('/')
    meta_data[PARENT_FOLDER] = parent_folder[-1]



    return meta_data


'''
Simple gateway to the ingestion app
'''

def _walk_directories_ingest_files(starting_dir_dict:dict,es_index:str):
    '''
    Do recursive walk of all files and folders in directory
    '''
    logging.info("Will ingest to elastic index:"+es_index)

    logging.debug("Starting Dict type:"+str(type(starting_dir_dict)))
    logging.debug("Starting Dict\n"+str(starting_dir_dict))


    #########
    # iterate over multiple directories
    #########
    for configsource,single_dir in starting_dir_dict.items():

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
                # Extact meta Data
                #########
                meta_data=_extract_metadata(configsource,full_filepath)


                #########
                # Check if this is a sub directory
                #########
                if(os.path.isdir(full_filepath)):
                    logging.info("Recursive call to handle directory:"+full_filepath)

                    #package as list
                    full_filepath_as_dict={}
                    full_filepath_as_dict[configsource]=full_filepath
                    _walk_directories_ingest_files(full_filepath_as_dict,es_index)


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
                    logging.info("Ignoring unknown format - format: "+filename)


            except Exception as problem:

                # decide how to handle it
                if config.read_boolean("CONTINUE_LOOP_AFTER_ERROR"):
                    # Log the error and continue loop
                    logging.exception(problem)
                    logging.info("\n Will attempt to continue loop as per config")

                else:
                    # rethrow the error and end
                    raise problem
            

            # add to index if we have text
            if(document_text==""):
                logging.info("No text extracted to index")
            else:
                logging.info("Indexing extracted text into Index")
                index_elastic.index(es_index_name,full_filepath,document_text,meta_data)
            
        



# simple code to run from command line
if __name__ == '__main__':

    #Set the Logging level. Change it to logging.INFO is you want just the important info
    #logging.basicConfig(filename=config.read("LOG_FILE"), encoding='utf-8', level=logging.DEBUG)
    logging.basicConfig(level=logging.DEBUG)


    # get config
    starting_point_dict = config.read_dict("SOURCE_DIRECTORIES")

    es_index=config.read("ES_INDEX_KB")
   

    #call the main method in this module
    _walk_directories_ingest_files(starting_point_dict, es_index)