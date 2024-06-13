import logging
import os
from typing import List, Optional

import settings.config as config
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
#from langchain_community.vectorstores import ElasticVectorSearch # replaced by next line
from langchain_elasticsearch import  ElasticsearchStore
from langchain_core.documents import Document

# Module level variables
character_text_splitter = None
model_transformers = None
hf = None
es_url= None

def _do_setup():
    '''
        carry out initial setup if needed
    '''

    global character_text_splitter
    global model_transformers
    global hf
    global es_url

    # check if we have been here before and can short circuit
    if (hf is not None):
        return

    logging.debug("carrying out setup of index module")


    character_text_splitter = CharacterTextSplitter(
        separator="\n\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
        is_separator_regex=False,
    )

    # get the model we need to encode the text as vectors (in Elastic)
    model_transformers = config.read("MODEL_TRANSFORMERS")
    logging.debug("Prep. Huggingface embedding setup using "+model_transformers)
    hf= HuggingFaceEmbeddings(model_name=model_transformers)

    # Get the elastic URL from settings
    # If we can to allow for username and password we can update to something like:
    # es_url =  f"https://{username}:{password}@{endpoint}:9200"
    # noting that the username, assword and endpoint should valid
    es_url =  config.read("ES_URL")
    logging.debug ("Using Elastic Service at URL "+es_url)



def _extract_pdf_and_meta(filepath: str,metadatas: Optional[dict])-> List[Document]:
    '''
    Index the specificed pdf (and document meta data) into the elastic index
    '''


    ## Langchain pdf splitting
    logging.debug("Loading and splitting:"+filepath)
    loader = PyPDFLoader(filepath)
    pages = loader.load_and_split()

    # Adding metadata to documents
    for page_counter, doc in enumerate(pages):

        #add known meta data
        doc.metadata["modified"] = os.path.getmtime(filepath) 
        doc.metadata["name"] = filepath
        doc.metadata["format"] = "pdf"
        doc.metadata["page"] = page_counter

        # loop through optional dict and add to doc
        for key, value in metadatas.items():
            doc.metadata[str(key)] = value

        logging.debug(f"Prep-d page {page_counter} text and meta") # - length"+str(len(doc.text)))

    return pages





def _extract_text_and_meta(filepath: str,filecontents: str,metadatas: Optional[dict])-> List[Document]:
    '''
    Index the specificed pdf (and document meta data) into the elastic index
    '''

    ## Langchain text-char splitting
    logging.debug("Loading and splitting:"+filepath)
    pages = character_text_splitter.create_documents([filecontents])


    # Adding metadata to each of these document / pages
    for page_counter, doc in enumerate(pages):
  
        file_extension = os.path.splitext(filepath)
        doc.metadata["format"] = file_extension
        
        doc.metadata["modified"] = os.path.getmtime(filepath) 
        doc.metadata["name"] = filepath
        doc.metadata["page"] = page_counter

        # loop through optional dict and add to doc
        for key, value in metadatas.items():
            doc.metadata[str(key)] = value

        logging.debug(f"Prep-d page {page_counter} text and meta - length")#+str(len(doc.text)))

    return pages





def index(index_name: str,filepath: str,filecontents: str,meta_data = {}) -> None:
    '''
    Index the specified text (and document meta data) into the elastic index
    '''
    #setup if we're here first time
    _do_setup()

    # Next we'll create our elasticsearch vectorstore in the langchain style:
    #es_index = ElasticVectorSearch(embedding=hf,elasticsearch_url=es_url, index_name=index_name) prev
    es_index= ElasticsearchStore(embedding=hf,es_url=es_url, index_name=index_name)




    ## Split our document body into pages using specific methods
    if filepath.lower().endswith(".pdf"):
        
        pages = _extract_pdf_and_meta(filepath,meta_data)
    else:
        pages = _extract_text_and_meta(filepath,filecontents,meta_data)
      

    # save the page-text-metadata into the es index
    es_index.from_documents(pages, embedding=hf, es_url=es_url, index_name=index_name)


    





