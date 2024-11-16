import logging
import sys
import unittest

import util.index.extract_email as extract_email
import index.extract_pdf as extract_pdf
import index.extract_word as extract_word

#sys.path.append('..')
import settings.config as config


class Test_File(unittest.TestCase):
   
    @classmethod
    def setUpClass(self):
       
        #setup logging
        logger = logging.getLogger("..")
        logger.setLevel(logging.DEBUG)
    
    def test_read_pdf(self):

        #check that we have a pandas dataframe, with one row plus header
        document_text_1 = extract_pdf.loop_extract_text_info_no_ocr("data-sample/ingest/ie-a-brief-guide-to-forming-a-company.pdf")
        self.assertIsNotNone(document_text_1)
        print(document_text_1)

        document_text_2= extract_pdf.loop_extract_text_info_with_ocr("data-sample/ingest/companyprofile.pdf")
        self.assertIsNotNone(document_text_2)
        print(document_text_2)

    def test_read_word(self):

        # Extract _extract_text_stats information
        document_text = extract_word.loop_extract_text_info_word("data-sample/ingest/word_file_sample.docx")
        self.assertIsNotNone(document_text)
        print(document_text)


    def test_read_email(self):

        document_text = extract_email.extract_text_info_general("data-sample/ingest/sample_test_outlook_file.msg")
        self.assertIsNotNone(document_text)

        #check that we have a pandas dataframe, with one row plus header
        self.fail("Not implemented yet")

if __name__ == '__main__':
    unittest.main()