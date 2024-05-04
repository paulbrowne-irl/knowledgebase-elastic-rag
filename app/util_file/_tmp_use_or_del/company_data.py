from dataclasses import dataclass,field

from typing import Dict

@dataclass
class company_data():
    """This is a data holder for the information we extract on a company"""

    #key_information_to_extract
    key_info: Dict[str, str] = field(default_factory = lambda: ({}))

    # tables(sheets) that we pull from pdf, and the (sheet) names we have identifed for them
    tables:  list = field(default_factory=lambda : [] , repr=False) #repr means it won't get printed out
    table_names:  list = field(default_factory=lambda : [])

    #working information - not as important
    original_pdf_name: str =""

    #nltk info and keywords
    keyword_info: list = field(default_factory=lambda : [])

   