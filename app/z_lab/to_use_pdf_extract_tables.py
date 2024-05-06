'''
Export and import Company information
'''

import logging
from pprint import pprint

import pandas as pd
import tabula
from pandas.core.frame import DataFrame

import company_data
import settings


def capture_information_from_pdf(filename:str)->company_data:
    '''
    Extract the information in the PDF into company_data object
    '''

    my_company=company_data.company_data()

    # make a note of the original pdf name
    my_company.original_pdf_name=filename

    # extract all the tables in the PDF file
    my_company.tables = tabula.read_pdf(filename, stream=True,pages='all')

    #Attempt two methods to read pdfs
    my_company.tables = tabula.read_pdf(filename,  multiple_tables=True,pages='all',lattice=False)

    if len(my_company.tables)<settings.LATTICE_THRESHOLD:

        logging.info("Number of tables less than "+str(settings.LATTICE_THRESHOLD)+" trying again using graphic lattice mode")

        # probably graphic tables embedded - try again using Lattice mode
        my_company.tables = tabula.read_pdf(filename,  multiple_tables=True,pages='all',lattice=False)
        my_company.key_info["Info Type"]="Probably Graphic"
    else:
        my_company.key_info["Info Type"]="Probably Table"



    
    # number of tables extracted
    logging.info("Total tables extracted from pdf:"+str(len(my_company.tables)))

    return my_company