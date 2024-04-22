import logging
import re
from collections import OrderedDict

import pandas as pd

import company_data
import settings


def identify_sheet_name(my_table: pd.DataFrame,counter:int)->str:
    '''
    Try and identify the sheet name for the contents of an excel table passed in
    '''

    sheetname=""+str(my_table.columns[0])

    #remove special characters and truncate
    sheetname= re.sub('[^A-Za-z0-9]+', '', sheetname)     
    sheetname = sheetname[:29]

    #default name
    if sheetname=="" or sheetname.find("Unnamed")>-1:
        #default
        sheetname="Sheet-"+str(counter)

    return sheetname


def update_sheet_names(my_company:company_data)->company_data:
    '''
    Loop through and modify sheet names
    '''

    #zip tables table names so we don't lose the link
    table_dict=dict(zip(my_company.table_names, my_company.tables))
    
    output_dict={}

    for table_name in table_dict.keys():

        found_flag=False

        #loop through our find replace
        for match in settings.TAB_FIND_REPLACE.keys():

            if (table_name.lower() == match.lower()) or (match.lower() in table_name.lower() ):

                #Add the existing sheet under the new name associated with the match
                output_dict[settings.TAB_FIND_REPLACE.get(match)]=table_dict.get(table_name)
                
                #print("matched:"+table_name.lower()+" to:"+match.lower()+" replacing with:"+settings.TAB_FIND_REPLACE.get(match))

                #break out of the loop
                found_flag=True
                break
       
        
        #if we get this far - add under a marker
        if(not found_flag):
            print("Adding default:"+"z_"+table_name)
            output_dict["z_"+table_name]=table_dict.get(table_name)[:29]

    # sort alphabetically
    output_dict = OrderedDict(sorted(output_dict.items()))
    output_dict = dict(output_dict)

    #Set the updated values back in company dto
    my_company.table_names= list(output_dict.keys())
    my_company.tables= list(output_dict.values())

    #Make a note of the sheet names in key info
    my_company.key_info["Sheet Names"]=str(output_dict.keys())[10:-1]
    
    return my_company


