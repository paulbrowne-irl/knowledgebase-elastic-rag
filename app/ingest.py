import logging
import os

import app.util_file.extract_general as extract_general
import app.util_file.extract_pdf as extract_pdf
import app.util_file.extract_word as extract_word
import settings.config as config


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

    #########
    # iterate over files in directory
    # including sub directories
    #########
    for filename in os.listdir(starting_dir):

        #reset document text
        document_text=""

        try:

            # Get the next file in this directory
            f = os.path.join(starting_dir, filename)

            #########
            # Check if this is a sub directory
            #########
            if(os.path.isdir(f)):
                logging.info("Recursive call to handle directory:"+f)
                walk_directory_ingest_files(f,es_index)

            #########
            # pdf
            #########
            elif filename.lower().endswith(".pdf"):

                logging.info("processing pdf file: "+filename)

                # Extract information using two methodologies
                document_text = extract_pdf.loop_extract_text_info_no_ocr(f)

                if(do_pdf_ocr):
                    document_text= document_text+extract_pdf.loop_extract_text_info_with_ocr(f)

                #logging.info("Extracted Text:"+document_text)

            #########
            # Word
            #########
            elif filename.lower().endswith(".docx"):
                logging.info("processing word file: "+filename)

                # Extract _extract_text_stats information
                document_text = extract_word.loop_extract_text_info_word(f)
            
            #########
            # Excel
            #########

            elif filename.lower().endswith(".xlsx"):
                logging.info("skipping excel file: "+filename)

            #########
            # General including emails
            #########

            else:
                logging.info("using generic format: "+filename)
                document_text = extract_general.extract_text_info_general(f)
                logging.info("found text:"+str(document_text))


        except Exception as problem:

            # decide how to handle it
            if config.read_boolean("CONTIUE_LOOP_AFTER_ERROR"):
                # Log the error and continue loop
                logging.error(problem)

            else:
                # rethrow the error and end
                raise problem
        
        finally:
            pass
            # add this as new row to output
            #new_record = pd.DataFrame([{'Case':filename, 'Size':len(document_text), 'Text':document_text}])
            #output_df = pd.concat([output_df, new_record], ignore_index=True)
            #logger.info("Added:"+str(counter)+" :"+filename+" :length "+str(len(document_text)))
            #logger.info("=================================================/n")

            #output_df.to_excel(settings.OUTPUT_TEXT_ANALSYIS, index=False)

        # add to index
        #TODO - extract meta data
        #TODO - add to index
        



# simple code to run from command line
if __name__ == '__main__':

    #Set the Logging level. Change it to logging.INFO is you want just the important info
    #logging.basicConfig(filename=config.read("LOG_FILE"), encoding='utf-8', level=logging.DEBUG)
    logging.basicConfig(level=logging.INFO)


    # get config
    starting_dir = config.read("SOURCE_DIR_FILES")
    es_index=config.read("ES_INDEX_KB")
   

    #call the main method in this module
    walk_directory_ingest_files(starting_dir, es_index)