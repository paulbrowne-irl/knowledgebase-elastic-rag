import unittest
import logging

import sys
sys.path.append('..')
import app.settings.config as config

class Test_XL(unittest.TestCase):
   
    @classmethod
    def setUpClass(self):
       
        #setup logging
        logger = logging.getLogger("..")
        logger.setLevel(logging.DEBUG)
    
    def test_read_xl(self):
        
        self.fail("Test not implented yet"))