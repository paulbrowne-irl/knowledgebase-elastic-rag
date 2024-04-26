import unittest
import logging
import os

import pandas as pd

import testsettings

# allow imports from parent directory
import sys
sys.path.append('../project_xl')
import util.table_names as table_names
import company_data

class Test_Util_Table(unittest.TestCase):
   
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

 
    def test_replace_table_name(self):
        
        test_comp=company_data.company_data()

        test_comp.table_names=['SustainingEnterpriseFundPropos', 'DepartmentManagerNameBillMcTosh', 'YE', 
                            'YEamendasperYE', 'TrackRecordProjectionsAcme', 'R and D', 'Employment', 'Depreciation', 'AcmeCorpCompanyGroup',
                            'Cashflow', 'AcmeCorpCompanyGroup', 'Financedby', 'Cashflow', '1COMPANYDETAILS', 'Contact', 'Declaration', 
                            'Isnotinthecourseofbeingwoundup', 'Project','1StateBanksGovernment2Haveyoua', 'DirectorName',  
                            'CHECKLISTOFINFORMATIONNEEDEDBY', 'ProjectCosts', 'ApplID','Tranche1Amount']
        
        #generate equiv amount of data frames
        for i in range(len(test_comp.table_names)):
            test_comp.tables.append(pd.DataFrame())

        test_comp=table_names.update_sheet_names(test_comp)

        print(test_comp.table_names)

        #checks that the substitions have been made as expected
        self.assertIn("Year End",test_comp.table_names)
        self.assertIn("Repayment Calc",test_comp.table_names)




unittest.main()

 