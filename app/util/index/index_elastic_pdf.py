# Imports
# Make sure the requirements are installed using pip install -r requirements.txt


from tqdm import tqdm
from langchain.embeddings import HuggingFaceEmbeddings

from getpass import getpass
from pathlib import Path
from langchain.vectorstores import ElasticVectorSearch
from langchain_community.vectorstores.elasticsearch import ElasticsearchStore
from langchain_community.document_loaders import PyPDFLoader

from pathlib import Path

import os
import fnmatch
import logging

import app.settings.config as config

# Module level setup - should be run only once

# Get the elastic URL from settings
# If we can to allow for username and password we can update to something like:
# es_url =  f"https://{username}:{password}@{endpoint}:9200"
# noting that the username, assword and endpoint should valid
es_url =  config.read("ES_URL")
logging.info ("Using URL "+config.read("ES_URL"))

# get the model we need to encode the text as vectors (in Elastic)
logging.debug("Prep. Huggingface embedding setup")
hf= HuggingFaceEmbeddings(model_name=config.read("LOCAL_MODEL_TRANSFORMERS"))

# Next we'll create our elasticsearch vectorstore in the langchain style:
db = ElasticVectorSearch(embedding=hf,elasticsearch_url=es_url, index_name=config.read("ES_INDEX_KB"))
#db = ElasticsearchStore(es_url,hf,index_name=config.read("ES_INDEX)


def index_text_and_meta_data(index_name: str,filename: str,filecontents: str) -> None:
        
    ## LANGCHAIN
    loader = PyPDFLoader(filename)
    pages = loader.load_and_split()

    # Adding metadata to documents
    for i, doc in enumerate(pages):
        doc.metadata["modified"] = os.path.getmtime(path) 
        doc.metadata["name"] = file
        doc.metadata["product"] = "SEF"
        doc.metadata["format"] = "PDF"
        doc.metadata["type"] = "Application"

        logging.debug("ES Indexing:"+str(len(eModel.text)))
        # was from text
        #   db.from_documents(eModel.toDocument(), embedding=hf, elasticsearch_url=es_url, index_name=settings.ES_INDEX )

        db.from_documents(pages, embedding=hf, elasticsearch_url=es_url, index_name=config.read("ES_INDEX_KB"))


#########

## json method
'''	
logging.debug("Name : " + str(eModel))

url = "http://localhost:9200/" + settings.ES_INDEX +"/_doc?pretty"
data = eModel.toJSON()

response = requests.post(url, data=data,headers={
                'Content-Type':'application/json',
                'Accept-Language':'en'

            })
logging.debug("Url : " + url)
logging.debug("Data : " + str(data))

logging.debug("Request : " + str(requests))
logging.debug("Response : " + str(response))
'''