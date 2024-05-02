import logging
import util_file.xl  as xl
import settings.config as config

'''
Simple gateway to the ingestion app
'''

def walk_directory_ingest_files():
    pass



# currently placeholder

# simple code to run from command line
if __name__ == '__main__':
    #Set the Logging level. Change it to logging.INFO is you want just the important info
    #logging.basicConfig(filename=config.read("LOG_FILE"), encoding='utf-8', level=logging.DEBUG)
    logging.basicConfig(level=logging.DEBUG)

    #call the main method in this module
    walk_directory_ingest_files()