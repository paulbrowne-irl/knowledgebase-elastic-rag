import logging

from pandas.core.frame import DataFrame

import pandas as pd

import os.path
import os

import app.settings.config as config

import util.file_import as file_import
import util.file_export as file_export
import util.file_util as file_util
import util.shape_data as shape_data
import util.table_names as table_names
import util.line_extract as line_extract


from company_data import company_data


def _loop_extract_key_info(my_company:company_data)->company_data:
    '''
    Loop through and extract key information from the tables in the document

    Operates on a company data object
    '''

    #check we have tables to loop through
    if (len(my_company.tables)>0):
        
        #loop through and extract key info
        for x in range (len(my_company.tables)):

            #decide sheet name
            sheetname=table_names.identify_sheet_name(my_company.tables[x],x)
            my_company.table_names.append(sheetname)

            #Extract key info
            line_extract.add_key_info_if_not_exists(my_company,my_company.tables[x],config.read("KEY_INFO_SEARCH"))

        # Now that we have all table names, check if we need to modify them
        my_company= table_names.update_sheet_names(my_company)

    else:
         logger.info("No tables found in pdf");

    return my_company


# simple code to run from command line
if __name__ == '__main__':
    
    #setup logging
    logger = logging.getLogger("")
    logger.setLevel(logging.INFO)

    #for testing - break after x goes
    counter=0
  
    # iterate over files in directory
    for filename in os.listdir(config.read("WORKING_FOLDER")):
        
        try:

            #Check if we should process this files
            if(file_util.should_we_process_this_file(filename)):
                logging.info("\nReading pdf:"+filename)
                
                #Get the next file in this directory
                f = os.path.join(config.read("WORKING_FOLDER"), filename)

                #Read the tables into the data structure
                my_company=file_import.capture_information_from_pdf(f)

                #Extract key information
                my_company= _loop_extract_key_info(my_company)

                #reshape the data so it is more useful in later analysis
                my_company= shape_data.reshape_data(my_company)

                #export information into the folder as Excel
                file_export.export_file(my_company)
                
                #break if this is set
                counter+=1
                if counter>=config.read_int("MAX_NUMBER_OF_FILES"):
                    logger.warning("ENDING AFTER CYCLE:"+str(config.read__int("MAX_NUMBER_OF_FILES")))
                    break


        except Exception as problem:


            #decide how to handle it
            if(config.read_boolean("CONTINUE_LOOP_AFTER_ERROR")):
                 #Log the error and continue loop
                logging.error(problem)
                
            else:
                #rethrow the error and end
                raise problem
