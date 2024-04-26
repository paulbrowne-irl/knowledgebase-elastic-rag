
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import ElasticVectorSearch

from langchain.prompts import PromptTemplate
#from langchain.chains import LLMChain
from langchain.chains.llm import LLMChain

from langchain_community.llms import HuggingFacePipeline
from transformers import AutoTokenizer
from transformers import pipeline
from transformers import AutoModelForSeq2SeqLM

from langchain_elasticsearch import ElasticsearchStore


#from langchain_community.vectorstores.elasticsearch import 
from langchain_elasticsearch import ApproxRetrievalStrategy


import logging


import settings.default
import settings.pickle_loader

import util.llm_copilot as llm_copilot


#Module level constants
_embeddings=None
_db={}
_llm=None
token=None

#Set the Logging level. Change it to logging.INFO is you want just the important info
#logging.basicConfig(filename=settings.default.LOG_FILE, encoding='utf-8', level=logging.DEBUG)

def setup():
    '''
    Initialise the system (if needed)
    Safe to call multiple types as checks if have been called prviously
    '''
    _setup_copilot_token()
    _setup_embeddings()
    _setup_llm()

def _setup_copilot_token(): 
   
    global token
 
    token = settings.pickle_loader.setup_copilot_token()


def _setup_embeddings(): 
    '''
    Setup the embeddings that we use for vector search
    '''
    global _embeddings
    
    if(_embeddings==None):
        print("Setting up Embeddings")

        _embeddings = HuggingFaceEmbeddings(model_name=settings.default.MODEL_TRANSFORMERS)
    else:
        print("Embeddings already setup")


def _setup_llm():
    
    global _llm
    global _embeddings

    if(_llm==None):
        
        print("Setting up LLMs - local")
        _llm={}

        # setup the LLM
        print(f"Setting up model {settings.MODEL_LLM} ready to go")
        tokenizer = AutoTokenizer.from_pretrained(settings.default.MODEL_LLM)
        model = AutoModelForSeq2SeqLM.from_pretrained(
            settings.default.MODEL_LLM, cache_dir=settings.default.CACHE_DIR)

        pipe = pipeline(
            "text2text-generation",
            model=model,
            tokenizer=tokenizer,
            max_length=100
        )
        _llm['Local LLM'] = HuggingFacePipeline(pipeline=pipe)


        print("Setting up LLMs - copilot")
        _llm ['Copilot']= llm_copilot.CustomLLM(copilot_token=token)


    else:

        print("LLM list already setup")


def _get_datastore(index_name):
    '''
    Setup Handle to the external RAG Datastore
    '''


    if(index_name not in _db):
        
        print("Setting up Datastore:"+index_name +" using embeddings:"+str(_embeddings))

        
        if(index_name=='UECS Emails'):
            index_to_use=settings.default.ES_INDEX_EMAILS
        else:
            index_to_use= settings.default.ES_INDEX_DOCUMENTS


        _db [index_name]=  ElasticsearchStore(embedding=_embeddings,es_url=settings.default.ES_URL, index_name=index_to_use,strategy=ApproxRetrievalStrategy())
        

    else:
        print("Using cached Datastore ")

    return  _db [index_name]


def get_nearest_match_documents(index_name:str,vector_search_text:str):
    '''
    Get the nearest match documents using vector search
    '''
    print(f"Nearest Search index {index_name} matching against {vector_search_text}")

    vector_search= _get_datastore(index_name)

    return vector_search.similarity_search(vector_search_text)



def get_llm_chain(llm_choice,prompt_template):
    '''
    Generate the LLM Chaim
    '''

    global _llm

    prompt_informed = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

    return LLMChain(prompt=prompt_informed, llm=_llm[llm_choice])

