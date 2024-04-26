'''
Export and import Company information
'''

import logging
from pprint import pprint

import pandas as pd
from pandas.core.frame import DataFrame

import company_data
import settings.default

import os.path
import os



def get_export_file_name(original_file_name:str)->str:
    '''
    Set the name of the export file
    '''
    
    export_file_name="dummy.xlsx"

    #strip off .pdf suffix
    if original_file_name.lower().endswith(".pdf"):
        export_file_name = original_file_name[:-4]
    
    #Add default extension
    export_file_name=export_file_name+settings.default.OUTPUT_APPEND

    return export_file_name



def export_file(my_company:company_data):
    '''
    export our company data object to an excel file
    '''


    #set the company name 
    f=get_export_file_name(my_company.original_pdf_name)
    logging.info("Setting export file to:"+f)

    pprint("About to export info:")
    pprint(my_company,depth=2)

    #Export information to excel
    with pd.ExcelWriter(f) as writer:  
             
        #loop through and export sheet names in workbook
        for x in range (len(my_company.tables)):

            #export the table, appending to existing open workbook
            my_company.tables[x].to_excel(writer, sheet_name=my_company.table_names[x],index=True)
            #logging.info("Exported Sheet:"+my_company.table_names[x])
