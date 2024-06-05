
import logging
from typing import (Any, Callable, Dict, Iterable, List, Literal, Optional,
                    Tuple, Union)

import settings.config as config
import settings.pickle_loader
import util.rag.llm_copilot as llm_copilot
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import HuggingFacePipeline, Ollama
from langchain_core.documents import Document
from langchain_elasticsearch import ApproxRetrievalStrategy, ElasticsearchStore
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline
from util.rag import llm_echo

#Module level constants
_embeddings=None
_kb_dict={}
_llm_to_use=None
_token=None


def setup():
    '''
    Initialise the system (if needed)
    Safe to call multiple types as checks if have been called prviously
    '''
    _setup_vector_embeddings()
    _setup_llm()




def _setup_copilot_token(): 
   
    global _token
 
    _token = settings.pickle_loader.setup_copilot_token()




def _setup_vector_embeddings(): 
    '''
    Setup the embeddings that we use for vector search
    '''
    global _embeddings
    
    if(_embeddings==None):
        logging.debug("Setting up Embeddings")
        
        model_name=config.read("MODEL_TRANSFORMERS")
        logging.debug("Attempting to use embeddings:"+model_name)

        _embeddings = HuggingFaceEmbeddings(model_name=model_name)
    else:
        logging.debug("Embeddings already setup")


def _setup_llm():
    
    global _llm_to_use
    global _embeddings

    if(_llm_to_use==None):

        # we need to set it up accoding to sessings
        MODEL_LLM=config.read("MODEL_LLM")
        logging.debug(f"Attmpting to setup LLM {MODEL_LLM}")

        if (MODEL_LLM =="llama3"):
            _llm_to_use = Ollama(model="llama3",stop=['<|eot_id|>'])

        elif (MODEL_LLM =="google/flan-t5-large"): 

            logging.debug("Setting google/flan-t5-large")
            tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-large")
            model = AutoModelForSeq2SeqLM.from_pretrained(
                config.read("google/flan-t5-large"), cache_dir=config.read("CACHE_DIR"))

            pipe = pipeline(
                "text2text-generation",
                model=model,
                tokenizer=tokenizer,
                max_length=100
            )
            
            _llm_to_use = HuggingFacePipeline(pipeline=pipe)

        elif (MODEL_LLM =="test"): 
            _llm_to_use = llm_echo.EchoLLM()

        else :
            logging.debug("Default LLM to copilot")
            _setup_copilot_token()
            _llm_to_use = llm_copilot.CopilotLLM(copilot_token=_token)
            


    else:

        logging.debug("LLM already setup")





def _get_knowledgebase(index_name:str)->dict:
    '''
    Setup Handle to the external RAG Datastore
    '''


    if(index_name not in _kb_dict):
        
        logging.debug("Setting up Elastic Knowledgebase:"+index_name +" using embeddings:"+str(_embeddings))

        
        if(not index_name=='Knowledgebase'):
            index_to_use= config.read("ES_INDEX_KB")

        else:
             index_to_use=config.read("ES_INDEX_EMAILS")

            

        _kb_dict [index_name]=  ElasticsearchStore(embedding=_embeddings,es_url=config.read("ES_URL"), index_name=index_to_use,strategy=ApproxRetrievalStrategy())
        

    else:
        logging.debug("Using cached Datastore ")

    return  _kb_dict [index_name]






def get_nearest_match_documents(index_name:str,vector_search_text:str)->List[Document]:
    '''
    Get the nearest match documents using vector search
    '''


    logging.debug(f"Nearest Search index {index_name} matching against {vector_search_text}")

    vector_search= _get_knowledgebase(index_name)

    return vector_search.similarity_search(vector_search_text)



def get_llm_chain(prompt_template:str)->LLMChain:
    '''
    Generate the LLM Chain
    '''

    global _llm_to_use

    prompt_informed = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

    return LLMChain(prompt=prompt_informed, llm=_llm_to_use)

