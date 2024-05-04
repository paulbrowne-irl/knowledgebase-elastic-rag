
import docx2txt

import logging
import os
import os.path


def loop_extract_text_info_word(filename: str) -> str:
    text = docx2txt.process(filename)

    return text