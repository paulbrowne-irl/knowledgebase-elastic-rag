import logging
import unittest
from pprint import pprint

import pytest
import service.service_redact as service_redact
from langchain_core.documents import Document
from rich.console import Console

console = Console()


class Test_Redact_Service(unittest.TestCase):
   
    @classmethod
    def setUpClass(cls):
       
        #setup logging
        logger = logging.getLogger("..")
        logger.setLevel(logging.DEBUG)

    def test_redact_document(self):

        #create document
        text_document = Document(
            page_content='''Peter Parker works as the CEO of a company called ACME engineering. He lives in Dublin and his phone number is 01-234567
            Diana Prince is the co-founder of a company called BionMedical . She lives in Galway and her phone number is 01-234567
            ''',
            metadata={"source": "local_est"}
        )
        print("Original:"+str(text_document))


        #test redact
        redacted_doc =  service_redact.redact_doc(text_document,"d1")

        print(f"\nUse the following anonymized text:\n{redacted_doc}")

        removed_info_summary = ', '.join(list(service_redact.redacted_mappings.keys()))
        print(f"\nRemoved sensitive information: {removed_info_summary}")

        #test restore
        deanonymized_doc = service_redact.deanonymize_doc(redacted_doc)

        print(f"\nPrivate information restored:\n{deanonymized_doc}\n")

        ##check all info restored i.e. no more tags
        assert str(deanonymized_doc).find("[d1-PERSON-1]")<0
        assert str(deanonymized_doc).find("[d1-PERSON-2]")<0
        assert str(deanonymized_doc).find("[d1-PRODUCT-1]")<0
        assert str(deanonymized_doc).find("[d1-ORG-1]")<0
        assert str(deanonymized_doc).find("[d1-GPE-2]")<0
        

        #repeat redact to check we get increment
        text_document2 = Document(
             page_content="Diana Prince is the co-founder of a company called BionMedical . She lives in Galway and her phone number is 01-234567",
             metadata={"source": "local_est"}
         )

        redacted_doc = service_redact.redact_doc(text_document2,"d2")

        # check the the keys and fvalues are being stored as we'd expect
        #print("\n\n\n")
        #pprint(service_redact.redacted_mappings)
        assert "ACME" in service_redact.redacted_mappings
        assert "Dublin" in service_redact.redacted_mappings
        assert "Galway" in service_redact.redacted_mappings

        #check keys
        assert "d1-GPE-1" in service_redact.redacted_mappings.values()
        #assert "d1-GPE-2" in service_redact.redacted_mappings.values()

if __name__ == '__main__':
    unittest.main()