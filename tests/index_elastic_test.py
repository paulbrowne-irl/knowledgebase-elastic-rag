import logging
import sys
import unittest

import app.util_file.extract_general as extract_general
import app.util_file.extract_pdf as extract_pdf
import app.util_file.extract_word as extract_word
import app.util_nlp.index_elastic_pdf as index_elastic_pdf
import app.util_nlp.index_elastic_text as index_elastic_text

sys.path.append('..')
import app.settings.config as config


class Test_Index(unittest.TestCase):
   
    @classmethod
    def setUpClass(self):
       
        #setup logging
        logger = logging.getLogger("..")
        logger.setLevel(logging.DEBUG)
    
    def test_index_text(self):

        index_elastic_text.index_text_and_meta_data()
        self.fail("full test not implemented")
    
    def test_index_pdf(self):

        index_elastic_text.index_text_and_meta_data()
        self.fail("full test not implemented")

if __name__ == '__main__':
    unittest.main()