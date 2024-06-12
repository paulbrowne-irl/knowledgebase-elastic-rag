import logging
import sys
import unittest

import util.index.index_elastic as index_elastic

sys.path.append('..')
import settings.config as config


class Test_Injest(unittest.TestCase):
   
    @classmethod
    def setUpClass(self):
       
        #setup logging
        logger = logging.getLogger("..")
        logger.setLevel(logging.DEBUG)
    


    def test_extract_meta_data(self):
        '''see if we can extract the metadata from a file'''
        
        self.fail("Test not implemented yet")





if __name__ == '__main__':
    unittest.main()