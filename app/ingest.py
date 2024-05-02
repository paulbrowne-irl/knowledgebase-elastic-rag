import logging
import util_file.xl  as xl
import settings.config as config

'''
Simple gateway to the ingestion app
'''

def walk_directory_ingest_files(starting_dir,es_index):
    '''
    Do recursive walk of all files and folders in directior
    '''
    
    
    logging.debug("starting directory:"+starting_dir)
    logging.debug("Will ingest to elastic index:"+es_index)




# currently placeholder

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