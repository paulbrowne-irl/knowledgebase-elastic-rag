import unittest
import logging

#import settings.config as config

import sys
sys.path.append('..')
import app.settings.config as config
import app.util_file.xl  as xl

class Test_XL(unittest.TestCase):
   
    @classmethod
    def setUpClass(self):
       
        #setup logging
        logger = logging.getLogger("..")
        logger.setLevel(logging.DEBUG)
    
    def test_read_filtered_xl(self):

        xl_file = xl.read_filtered_xl("data-sample/question_and_answer/q_and_a_sample.xlsx")
        print(xl_file)
        
        self.fail("Test not implented yet")

if __name__ == '__main__':
    unittest.main()