import unittest
import logging
import os



class Test_LC_Controller(unittest.TestCase):
   
    @classmethod
    def setUpClass(cls):
       
        #setup logging
        logger = logging.getLogger("..")
        logger.setLevel(logging.DEBUG)
    
        #setup rag controller
    
    def test_rag(self):
        #self.fail("Tests not yet implemented")
        logging.debug("test completed")
