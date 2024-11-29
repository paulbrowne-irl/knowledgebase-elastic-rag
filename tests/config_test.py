import logging
import unittest
from pprint import pprint

import pytest
from rich.console import Console
import settings.config as config

console = Console()


class Test_Config_Read(unittest.TestCase):
    '''
     pytest -k Test_Config_Read
    '''
   
    @classmethod
    def setUpClass(cls):
       
        #setup logging
        logger = logging.getLogger("..")
        logger.setLevel(logging.DEBUG)


    def test_read_config(self):

        starting_point_dict = config.read_dict("SOURCE_DIRECTORIES")
        logging.info("Injesting files from root dir(s):"+str(starting_point_dict)+"\n")


if __name__ == '__main__':
    unittest.main()