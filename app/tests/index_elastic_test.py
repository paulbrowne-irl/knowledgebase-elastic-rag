import logging
import sys
import unittest

import util.index.index_elastic as index_elastic

sys.path.append('..')
import settings.config as config


class Test_Index(unittest.TestCase):
   
    @classmethod
    def setUpClass(self):
       
        #setup logging
        logger = logging.getLogger("..")
        logger.setLevel(logging.DEBUG)
    


    def test_index_text(self):

        test_meta =	{
            "key1": "value1",
            "key2": "value2",
            "key3": 1964
        }

        #try call
        index_elastic.index(index_name= "test",filepath="file.pdf" ,filecontents="",meta_data=test_meta)
        # no exception is success - update?



    def test_index_pdf(self):

        index_elastic.index(index_name= "test",filepath="file.msg" ,filecontents="XYZ")
        # no exception is success - update?



if __name__ == '__main__':
    unittest.main()