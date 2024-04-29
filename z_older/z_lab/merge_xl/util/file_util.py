import os.path
import os

import logging

import util.file_export as file_export

import app.settings.config as config

def should_we_process_this_file(original_file_name:str)->bool:
    ''' 
    Check if we should process this file.
    Reasons why we wouldn't include - not a PDF, includes "minute" in the name or export file already exists
    '''

    if not original_file_name.lower().endswith(".pdf"):
        logging.info("Ignoring non-pdf file: "+original_file_name)
        return False
    
    if  "minute" in original_file_name.lower():
        logging.info("Ignoring minutes file: "+original_file_name)
        return False
    
    # check that file already exists
    output_file_name=file_export.get_export_file_name(original_file_name)
    f = os.path.join(config.read("WORKING_FOLDER"), output_file_name)
    if os.path.isfile(f):
        logging.info("Ignoring file: "+original_file_name + " as output already generated in "+output_file_name)
        return False
    
    #if we get this far
    return True

