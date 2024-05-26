import unittest
import logging
import settings.config as config

import sys

from util.office import xl_rw
sys.path.append('..')

#import util.office.xl_rw  as xl_rw

class Test_XL(unittest.TestCase):
   
    @classmethod
    def setUpClass(self):
       
        #setup logging
        logger = logging.getLogger("..")
        logger.setLevel(logging.DEBUG)

        # read standard values
        self.QUESTION_FILE_NAME=config.read("QUESTION_FILE_XLS")
        self.COL_TO_READ_QUESTION_IN_FILE=config.read("COL_TO_READ_QUESTION_IN_FILE")
        self.COL_TO_UPDATE_RELEVANT_DOCS=config.read("COL_TO_UPDATE_RELEVANT_DOCS")
        self.COL_TO_UPDATE_SUGGESTED_ANSWER=config.read("COL_TO_UPDATE_SUGGESTED_ANSWER")

    
    def test_read_next_xl_question(self):

        next_question = xl_rw.read_next_unanswered_question("../data-sample/question_and_answer/q_and_a_sample.xlsx",
                                                            self.COL_TO_READ_QUESTION_IN_FILE,
                                                            self.COL_TO_UPDATE_SUGGESTED_ANSWER)
        logging.debug("next q:"+str(next_question))

        #check that we have a pandas dataframe, with one row plus header
        self.assertIsNotNone(next_question)

    def test_has_next_xl_question(self):

        has_next_question = xl_rw.has_unaswered_question("../data-sample/question_and_answer/q_and_a_sample.xlsx",
                                                            self.COL_TO_UPDATE_SUGGESTED_ANSWER)
      

        #check that we have a pandas dataframe, with one row plus header
        self.assertTrue(has_next_question)


if __name__ == '__main__':
    unittest.main()