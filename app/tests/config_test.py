import unittest
import logging

import sys
sys.path.append('..')
import settings.config as config

class Test_Config(unittest.TestCase):
   
    @classmethod
    def setUpClass(self):
       
        #setup logging
        logger = logging.getLogger("..")
        logger.setLevel(logging.DEBUG)

        #setup test class
    
    def test_config(self):
        
        self.assertEqual('"."',config.read("WORKING_DIRECTORY"))

    def test_config_int(self):
        self.assertTrue(0!=config.read_int("BREAK_AFTER_X_MAILS"))

    def test_config_boolean(self):
        flag = config.read_boolean("CONTINUE_LOOP_AFTER_ERROR")
        self.assertTrue(flag or not(flag))



    def test_all_values(self):
        all_values = dict(config.config.items('SETTINGS'))
        self.assertIsNotNone(all_values)
        print (all_values)



    def test_config_boolean(self):
        dict_values = config.read_dict("SOURCE_DIRECTORIES")

        self.assertIsNotNone(dict_values)
        self.assertEqual(len(dict_values),2)
        self.assertEqual(dict_values["SOURCE_DIR_FILES1"],"../data-sample/sub_dir_1")
        self.assertEqual(dict_values["SOURCE_DIR_FILES2"],"../data-sample/sub_dir_2")

