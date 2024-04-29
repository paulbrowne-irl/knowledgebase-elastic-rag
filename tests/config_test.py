import unittest
import logging

import app.settings.config as config

class Test_Config(unittest.TestCase):
   
    @classmethod
    def setUpClass(self):
       
        #setup logging
        logger = logging.getLogger("..")
        logger.setLevel(logging.DEBUG)

        #setup test class
    
    def test_config(self):
        
        self.assertEqual('"."',config.read("WORKING_DIRECTORY"))
        
        