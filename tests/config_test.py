import unittest
import logging
import os

# allow imports from parent directory
import sys
#sys.path.append('../util')


class Test_Config(unittest.TestCase):
   
    @classmethod
    def setUpClass(self):
       
        #setup logging
        logger = logging.getLogger("..")
        logger.setLevel(logging.DEBUG)

        #setup test class
    
    def test_config(self):
        self.fail("testing of pickle values not yet implemented")
        print("test completed")
