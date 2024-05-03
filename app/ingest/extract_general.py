
import textract

import logging
import os
import os.path


def extract_text_info_general(filename: str) -> str:
    '''
    Catch all method for extracting info using textract
    '''
    
    text = textract.process(filename)

    return text