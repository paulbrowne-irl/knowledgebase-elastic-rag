import logging
import unittest

import pytest
import os

import util.index.index_elastic as index_elastic
import settings.config as config

#@pytest.mark.skip
class Test_Index_Into_Elastic(unittest.TestCase):
    '''
    pytest -k Test_Index_Into_Elastic
    '''
   
    @classmethod
    def setUpClass(cls):
       
        #setup logging
        logger = logging.getLogger("..")
        logger.setLevel(logging.DEBUG)

    def test_index_word(self):

        test_meta =	{
            "key1": "value1",
            "key2": "value2",
            "key3": 1964
        }

   
        #try call
        index_elastic.index(index_name= "test-can-del",filepath="./data-sample/ingest/sub_dir_2/word_file_sample.docx" ,filecontents="blah blah blah",meta_data=test_meta)
        # no exception is success - update?

    def test_index_message(self):

        test_meta =	{
            "key1": "value1",
            "key2": "value2",
            "key3": 1964
        }

   
        #try call
        index_elastic.index(index_name= "test-can-del",filepath="./data-sample/ingest/sub_dir_2/sample_test_outlook_email.msg" ,filecontents="blah blah blah",meta_data=test_meta)
        # no exception is success - update?
    

    def test_index_text(self):

        test_meta =	{
            "key1": "value1",
            "key2": "value2",
            "key3": 1964
        }

   
        #try call
        index_elastic.index(index_name= "test-can-del",filepath="./data-sample/ingest/_docs.txt" ,filecontents="blah blah blah",meta_data=test_meta)
        # no exception is success - update?

    def test_index_pdf(self):

        test_meta =	{
            "key1": "value1",
            "key2": "value2",
            "key3": 1964
        }

        index_elastic.index(index_name= "test-can-del",filepath="./data-sample/ingest/sub_dir_1/guide-to-company-formation-ireland.pdf" ,filecontents="blah blah blah",meta_data=test_meta)
        # no exception is success - update?



if __name__ == '__main__':
    unittest.main()