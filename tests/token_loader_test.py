import unittest
import logging
import settings.token_loader as token_loader

import pytest


class Test_Secret_Value_Loader(unittest.TestCase):
   
    @classmethod
    def setUpClass(cls):
       
        #setup logging
        logger = logging.getLogger("..")
        logger.setLevel(logging.DEBUG)

        #setup test class

    def test_pickle_loader(self):
        token = token_loader.setup_token("some value")
        self.assertIsNotNone(token)
