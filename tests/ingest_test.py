import logging
import sys
import unittest

import app.ingest as ingest

sys.path.append('..')
import app.settings.config as config


class Test_Injest(unittest.TestCase):
   
    @classmethod
    def setUpClass(self):
       
        #setup logging
        logger = logging.getLogger("..")
        logger.setLevel(logging.DEBUG)
    


    def test_extract_meta_data(self):
        '''see if we can extract the metadata from a file'''

        outputDict= ingest._extract_metadata("SOME_CONFIG_SOURCE","../data-sample/ingest/companyprofile.pdf")
        
        self.assertEqual(outputDict.get(ingest.DATA_SOURCE),"SOME_CONFIG_SOURCE")
        self.assertEqual(outputDict.get(ingest.FILE_NAME),"companyprofile.pdf")
        self.assertEqual(outputDict.get(ingest.PARENT_FOLDER),"ingest")
        




if __name__ == '__main__':
    unittest.main()