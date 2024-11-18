import logging
import unittest
from pprint import pprint

import pytest
import service.service_email as service_email
from langchain_core.documents import Document
from rich.console import Console

console = Console()


class Test_Email_Service(unittest.TestCase):
   
    @classmethod
    def setUpClass(cls):
       
        #setup logging
        logger = logging.getLogger("..")
        logger.setLevel(logging.DEBUG)


    @pytest.mark.skip
    def test_generate_email(self):

        email_text="write me an email about dogs"
        email_drafted= service_email.draft_email_response(email_text)

        print(email_drafted)


if __name__ == '__main__':
    unittest.main()