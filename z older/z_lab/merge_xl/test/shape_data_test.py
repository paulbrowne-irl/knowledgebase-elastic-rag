# allow imports from parent directory
import sys
sys.path.append('../project_xl')

import logging
import os


import unittest
from pprint import pprint

import pandas as pd
import settings_test

import util.shape_data as shape_data

import company_data


class Test_Reshape_Data(unittest.TestCase):
   
    @classmethod
    def setUpClass(self):
       
        #setup logging
        logger = logging.getLogger("..")
        logger.setLevel(logging.DEBUG)

        if(not os.path.isfile(settings_test.TEST_BALANCE_SHEET)):
            raise Exception("Expected Test Data not found")

        #get the dataframe
        df_balance_sheet = pd.read_excel(settings_test.TEST_BALANCE_SHEET)
        my_company=company_data.company_data()
        my_company.tables=[df_balance_sheet]
        my_company.table_names=["Balance Sheet"]

        self.test_company=my_company



    def test_add_key_details_to_dataframe(self):

        self.assertIsNotNone(self.test_company)

        # Add two bits of key info
        self.test_company.key_info["CES ID Number"]=12345
        self.test_company.key_info["Company Legal Name"]="Acme Corp"

        #add these to our test data
        my_company = shape_data._add_key_details_to_dataframe(self.test_company)

        column_names = my_company.tables[0].columns.values.tolist()

        #Check that our company names have been added
        self.assertIn("CES ID Number",column_names)
        self.assertIn("Company Legal Name",column_names)
    





unittest.main()

 