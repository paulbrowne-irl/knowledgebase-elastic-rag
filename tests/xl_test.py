import unittest
import logging

import app.settings.config as config


import sys
sys.path.append('..')
import app.settings.config as config
import util_file.xl as xl

class Test_XL(unittest.TestCase):
   
    @classmethod
    def setUpClass(self):
       
        #setup logging
        logger = logging.getLogger("..")
        logger.setLevel(logging.DEBUG)
    
    def test_read_xl(self):

        xl_file = xl.read_xl("")
        print(xl_file)
        
        self.fail("Test not implented yet")