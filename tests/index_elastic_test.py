import logging
import unittest

import util.index.index_elastic as index_elastic
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
        index_elastic.index(index_name= "test-can-del",filepath="../data-sample/ingest/sample_test_outlook_email.msg" ,filecontents="blah blah blah",meta_data=test_meta)
        # no exception is success - update?



    def test_index_pdf(self):

        index_elastic.index(index_name= "test-can-del",filepath="../data-sample/ingest/companyprofile.pdf" ,filecontents="doh ray me fah so la tee doh")
        # no exception is success - update?



if __name__ == '__main__':
    unittest.main()