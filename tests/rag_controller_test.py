import unittest
import logging
import os

# allow imports from parent directory
import sys
#sys.path.append('../util')


class Test_Rag_Controller(unittest.TestCase):
   
    @classmethod
    def setUpClass(self):
       
        #setup logging
        logger = logging.getLogger("..")
        logger.setLevel(logging.DEBUG)

        #setup rag controller
    
    def test_dummy(self):
        self.fail("Tests not yet implemented")
        print("test completed")
