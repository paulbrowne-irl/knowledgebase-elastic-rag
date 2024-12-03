import logging
import unittest

from streamlit.testing.v1 import AppTest
import pytest



class Test_app_page_1(unittest.TestCase):
    '''
    pytest -k Test_app_page_1
    '''
   
    @classmethod
    def setUpClass(cls):
       
        #setup logging
        logger = logging.getLogger("..")
        logger.setLevel(logging.DEBUG)
    

    def test_page_load_emails(self):
        '''see if we can extract the metadata from a file'''
        at = AppTest.from_file("../app/pages/1_Respond_to_an_email.py").run()
        at.number_input[0].increment().run()
        at.button[0].click().run()
        assert at.markdown[0].value == "Beans counted: 1"




if __name__ == '__main__':
    unittest.main()