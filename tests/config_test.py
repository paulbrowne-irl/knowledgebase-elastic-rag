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
        print("read file:"+str(starting_point_dict)+"\n")

        assert isinstance(starting_point_dict, dict)
        assert len(starting_point_dict)>2 , "While this number may evolve, config should only return two values (dirs) in dictionary"

    def test_read_single_value(self):

        working_dir = config.read("ES_INDEX_KB")
        assert working_dir==".", "Unexpected value for working dir - have you changed it"



if __name__ == '__main__':
    unittest.main()