import unittest
import logging

import app.service.service_redact as service_redact

#to operate nroammly
import sys
sys.path.append('..')




class Test_Redact_Service(unittest.TestCase):
   
    @classmethod
    def setUpClass(self):
       
        #setup logging
        logger = logging.getLogger("..")
        logger.setLevel(logging.DEBUG)

    
    def test_redact_document(self):

            #text
            text="Peter Parker works as the CEO of a company called Spidercraft engineering. He lives in Dublin and his phone number is 01-234567"
            print("\n\nOriginal:"+text)


            #test redact
            redacted_text = service_redact.redact_text(text)

            print(f"\nUse the following anonymized text:\n{redacted_text}")

            removed_info_summary = ', '.join(list(service_redact.redacted_mappings.keys()))
            print(f"\nRemoved sensitive information: {removed_info_summary}")

            #test restore
            deanonymized_text = service_redact.deanonymize_text(redacted_text)

            print(f"\nPrivate information restored:\n{deanonymized_text}\n")

   

if __name__ == '__main__':
    unittest.main()