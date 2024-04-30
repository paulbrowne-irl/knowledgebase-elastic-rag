'''
Util file to read and write excel file
'''




# ################

import logging
import traceback
from pandas.core.frame import DataFrame


import pandas as pd


import app.settings.config as config


from tqdm import tqdm
from langchain.embeddings import HuggingFaceEmbeddings


from langchain.vectorstores import ElasticVectorSearch
from langchain_community.vectorstores.elasticsearch import ElasticsearchStore
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter

import fnmatch


'''
Index Mails (stored in Excel Sheet) to Elastic stack
'''


def read_xl(xl_file_name):
    
    #root_folder = .Folders.Item(1)
    print("Getting handle to Excel with Emails");
    email_table = pd.read_excel(xl_file_name, index_col=0) 

    return email_table

