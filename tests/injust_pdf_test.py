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

        xl_file = xl.read_next_unanswered_question("data-sample/question_and_answer/q_and_a_sample.xlsx")
        logging.debug(xl_file)

        #check that we have a pandas dataframe, with one row plus header
        self.assertEqual(2,len(xl_file.index))

if __name__ == '__main__':
    unittest.main()