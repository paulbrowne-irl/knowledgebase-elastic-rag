import re

import docx2txt


def loop_extract_text_info_word(filename: str) -> str:
    text = docx2txt.process(filename)

    # remove special charaters
    text = re.sub("[|'’€$@%–&•*/]", "", text)

    return text