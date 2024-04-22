# Scripts to get specfic details (lines in a table)

import pandas as pd
import logging

from typing import List

import company_data


def add_key_info_if_not_exists(my_company:company_data,my_table: pd.DataFrame,search_for_values:List[str]):
    '''
    Search for values and extract them to the cover sheet
    '''

    for search in search_for_values:

        #check if we've already got this value or not
        if(not search in my_company.key_info):
            
            #see if we have match
            matched_value=_search_for_line(my_table, search)
            if(matched_value!="" and matched_value is not None):
                my_company.key_info[search]=_tidy_matched_value(search,matched_value)
                logging.info("Added Key Info "+search+" :"+matched_value)


def _tidy_matched_value(search_value:str,found_line:str)->str:
    '''
    Remove the matched text key from the line (value)
    So it is tidier when we view in excel
    '''

    #Step one - remove the first part
    updated_value=found_line[len(search_value):]
    
    #step 2 Remove special leading charagers
    updated_value= updated_value.lstrip(" :")

    return updated_value



def _search_for_line(my_table: pd.DataFrame,search_for_value:str) -> str:
    '''
    see if we can find the value in the given table
    '''
    
    #set default
    matched_value=""

    #try to match on first column
    first_col=my_table.columns[0]
    matched_df = my_table[my_table[first_col].astype(str).str.contains(search_for_value,na=False)]
    
    

    if not matched_df.empty:

        
        #take value from first line
        matched_value=str(matched_df.iloc[0,0])

    
    return matched_value