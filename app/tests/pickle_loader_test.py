import unittest
import logging
import settings.pickle_loader as pickle_loader

# allow imports from parent directory
import sys


class Test_Pickle_Loader(unittest.TestCase):
   
    @classmethod
    def setUpClass(self):
       
        #setup logging
        logger = logging.getLogger("..")
        logger.setLevel(logging.DEBUG)

        #setup test class
    
    def test_pickle_loader(self):
        token = pickle_loader.setup_copilot_token()
        self.assertIsNotNone(token)
