import logging
import unittest
from pprint import pprint

import pytest
import service.service_email as service_email
from langchain_core.documents import Document
from rich.console import Console

console = Console()


class Test_Email_Service(unittest.TestCase):
    '''
    pytest -k Test_Email_Service
    '''
   
    @classmethod
    def setUpClass(cls):
       
        #setup logging
        logger = logging.getLogger("..")
        logger.setLevel(logging.DEBUG)


    def test_generate_email(self):

        email_text="I am curious about the new grant. How much can I claim and how it will it help me develop my business in international markets?"
        email_drafted= service_email.draft_email_response(email_text)

        print(email_drafted)

        #basic tests
        assert email_drafted != ""
        assert email_drafted is not None
        


if __name__ == '__main__':
    unittest.main()