import unittest
import logging
import settings.token_loader as token_loader


class Test_Pickle_Loader(unittest.TestCase):
   
    @classmethod
    def setUpClass(self):
       
        #setup logging
        logger = logging.getLogger("..")
        logger.setLevel(logging.DEBUG)

        #setup test class
    
    def test_pickle_loader(self):
        token = token_loader.setup_token("some value")
        self.assertIsNotNone(token)
