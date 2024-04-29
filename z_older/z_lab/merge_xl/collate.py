import logging

import openpyxl

import pandas as pd

import os.path
import os

import app.settings.config as config


'''
Utility to collate information from the .xlsx files generated by capture.py
In general, we will do this in Excel or Power Query - but useful for extracting data during developement
'''

def _rename_columns(thisDF:pd.DataFrame)->pd.DataFrame:
    '''
    Align the columns in two data frames so that the can easily be merges
    '''

    #check  for empty dataframe
    if thisDF.empty:
        return thisDF

    #Create empty name list
    col_name_list=[]
    for x in range(len(thisDF.columns)):
        col_name_list.append("col_"+str(x))
   
    #do the actual rename
    thisDF.set_axis(col_name_list, axis='columns', inplace=True)
    
    return thisDF

def _remove_duplicated_index_columns(thisDF:pd.DataFrame)->pd.DataFrame:
    '''
    test for and remove duplicate index
    ''' 

    #For checking if we got a clear run
    dropped_flag=False

    for x in range(len(thisDF.columns)):
        test_vals= str(thisDF.iloc[:,x].head(5).to_list()) 

        #logging.debug("Checking ... "+test_vals)

        if("[0, 1, 2, 3, 4]"==test_vals):
            
            #drop the column now
            #logging.debug("Dropped Column")
            thisDF.drop(thisDF.columns[x], axis = 1,inplace=True)

            #make a note we may want to go around again
            dropped_flag = True

            #Break out of the loop
            break
    
    #Check if we need to go around again
    if dropped_flag == True:
        #logging.debug("Do recursive call")
        thisDF=_remove_duplicated_index_columns(thisDF)
    else:
        #logging.debug("clear run - finished")
        pass

    return thisDF


def _merge_dataframes(mainframe:pd.DataFrame,df_to_add:pd.DataFrame)->pd.DataFrame:
    '''Merge two dataframes based on column alignment
    e.g. col to col1 - regardless of names'''
    
    #Remove any duplicated index cols
    mainframe= _remove_duplicated_index_columns(mainframe)
    df_to_add=_remove_duplicated_index_columns(df_to_add)
    
    #rename to sure the column names align
    mainframe = _rename_columns(mainframe)
    df_to_add = _rename_columns(df_to_add)


    #Merge the two sheets
    mergeDF = pd.concat([mainframe, df_to_add], ignore_index=True)

    return mergeDF

def _get_skip_list()->list:
    '''
    Get a list of already processed files that we will skip later
    '''

    df = pd.read_excel(config.read("PROCESSED_FILE_LIST")) 
    return  list(df.iloc[:,0])


# simple code to run from command line
if __name__ == '__main__':
    
    #setup logging
    logger = logging.getLogger("")
    logger.setLevel(logging.DEBUG)

    #for testing - break after x goes in settings
    counter=0

    # get the list of previously 
    skip_list = _get_skip_list()
  
    # iterate over files in directory
    for thisFile in os.listdir(config.read("WORKING_FOLDER")):
        
        #Get the next file in this directory
        f = os.path.join(config.read("WORKING_FOLDER"), thisFile)

        # checking if it is an xlsx Output file
        if os.path.isfile(f) and thisFile.lower().endswith(config.read("OUTPUT_APPEND")):

       
            # check if we have already processed this file
            if str(thisFile) in skip_list or thisFile.startswith("Collate"):
                logging.info("skipping already processed file:"+f)
                continue #next in file loop
            else:
                logging.info("\nReading xls file:"+f)
                inputWB = pd.ExcelFile(f)

            
            #Get sheet names as list
            for thisTab in inputWB.sheet_names:
               
                sheetToMerge = inputWB.parse(thisTab)

                #skip if start with ...
                if str(thisTab).startswith("z_"):
                    logging.debug("Skipping Tab :"+str(thisTab))
                    continue # go to next tab in loop
                else: 
                     logging.debug ("Processing tab:"+str(thisTab))

                #skip keywords as they can get quite big
                if str(thisTab).startswith("Keywords"):
                    logging.debug("Skipping Keywords")
                    continue # go to next item in loop

                #if needed add file name to key info and info
                if str(thisTab) == "Key Info" :
                    sheetToMerge["FileName"]=str(thisFile)

                #Generate the file name associated with this
                Outputfile=config.read("OUTPUT_COLLATE")+thisTab+".xlsx"
                OutputfileFull= os.path.join(config.read("WORKING_FOLDER"), Outputfile)
                
                #(if not exists) create an empty file associated with this outputfile
                if not os.path.isfile(OutputfileFull):
                    logging.debug("Creating new Workbook:"+Outputfile)
                    wb = openpyxl.Workbook()
                    wb.save(OutputfileFull)
                    wb.close
                
                #Now we know the file exists open it
                outputXL =  pd.read_excel(OutputfileFull)
                
                #merge the two sheets
                mergeDF = _merge_dataframes(outputXL,sheetToMerge)

                #overwrite with new values
                mergeDF.to_excel(OutputfileFull)
                

            #Close input file (we may have processed mutiple tabs)
            inputWB.close


            #break if this is set
            counter+=1
            if counter>=config.read_int("MAX_NUMBER_OF_FILES"):
                logging.info("Stopping after max number of files:"+str(config.read_int("MAX_NUMBER_OF_FILES")))
                break
                
        else:
             logging.info("Ignoring file:"+thisFile)