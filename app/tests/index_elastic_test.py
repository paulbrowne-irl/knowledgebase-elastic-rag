import logging
import sys
import unittest

import app.util.extract.extract_email as extract_email
import util.extract.extract_pdf as extract_pdf
import util.extract.extract_word as extract_word
import util.index.index_elastic as index_elastic

sys.path.append('..')
import settings.config as config


class Test_Index(unittest.TestCase):
   
    @classmethod
    def setUpClass(self):
       
        #setup logging
        logger = logging.getLogger("..")
        logger.setLevel(logging.DEBUG)
    
    def test_index_text(self):

        index_elastic.index_text_and_meta_data()
        self.fail("full test not implemented")
    
    def test_index_pdf(self):

        index_elastic.index_pdf_and_meta_data()
        self.fail("full test not implemented")

if __name__ == '__main__':
    unittest.main()