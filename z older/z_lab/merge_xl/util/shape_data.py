import logging
from pprint import pprint

import pandas as pd
from pandas.core.frame import DataFrame

import company_data
import settings.default
import util.table_names as table_names


def reshape_data(my_company:company_data)->company_data:
    '''
    Rearrange the format of our information to make it more useful for Excel later
    This depends on having all the info available (e.g. Company Name, ID - hence we do it as a second pass)
    '''

    # add key data to each table - makes later analyis easier
    my_company = _add_key_details_to_dataframe(my_company)

    # put other key info into sheet
    my_company.key_info["Original File Name"]=my_company.original_pdf_name

    # Insert the key info as the first sheet
    df=pd.DataFrame(my_company.key_info,index=[0])
    df=df.transpose()
    my_company.tables.insert(0,df) 
    my_company.table_names.insert(0,settings.default.KEY_INFO_OUTPUT_TAB_NAME)

    # insert the keywords as the second sheet
    my_company.tables.insert(1,my_company.keyword_info) 
    my_company.table_names.insert(1,settings.default.KEY_WORDS_OUTPUT_TAB_NAME)

    #return the info
    return my_company


def _add_key_details_to_dataframe(my_company:company_data)->company_data:
    '''
    See if can add specified data to the dataframe - makes it easier for later analysis
    '''


    #reverse the key data we add as columns
    #this means columns will be added to the spreadhseet in the order they appear in the settings
    reverse_add_info_list=reversed(settings.default.ADD_INFO_TO_ALL_SHEETS)

    # See if we have relevant info to add to data
    for key_data in reverse_add_info_list :
        if key_data in my_company.key_info:
            
            #now loop through and all columns to tables
            for x in range (len(my_company.tables)):

                #Loop through the keys and insert
                my_company.tables[x].insert(0,key_data,my_company.key_info.get(key_data))
    

    return my_company