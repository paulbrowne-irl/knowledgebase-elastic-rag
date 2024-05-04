import unittest
import logging

#import settings.config as config

import sys
sys.path.append('..')
import app.settings.config as config


class Test_XL(unittest.TestCase):
   
    @classmethod
    def setUpClass(self):
       
        #setup logging
        logger = logging.getLogger("..")
        logger.setLevel(logging.DEBUG)
    
    def test_read_pdf(self):

        #check that we have a pandas dataframe, with one row plus header
        self.fail("Not implemented yet")

    def test_read_word(self):

        #check that we have a pandas dataframe, with one row plus header
        self.fail("Not implemented yet")
    
    def test_read_email(self):

        #check that we have a pandas dataframe, with one row plus header
        self.fail("Not implemented yet")

if __name__ == '__main__':
    unittest.main()