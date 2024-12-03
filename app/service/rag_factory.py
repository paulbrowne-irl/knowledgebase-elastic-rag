import logging
from typing import (List)

import util.llm.llm_copilot as llm_copilot
import util.llm.llm_echo as llm_echo
import requests
import settings.config as config
import settings.token_loader as token_loader

from langchain_core import utils as langchain_core_utils
from langchain.chains.llm import LLMChain
from langchain.output_parsers.openai_functions import JsonOutputFunctionsParser
from langchain.prompts import PromptTemplate
from langchain_anthropic import ChatAnthropic
from langchain_community.llms import HuggingFacePipeline #, Ollama
from langchain_ollama import OllamaLLM
from langchain_core.documents import Document
from langchain_core.retrievers import BaseRetriever
from langchain_elasticsearch import DenseVectorStrategy, ElasticsearchStore
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_openai import ChatOpenAI
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline


'''
Helper class to support the various elements needed in a Langchain system 
'''

# Module level constants
_knowledgebase_retriever_dict = {}
_embeddings = None
_llm_to_use = None



def _get_setup_vector_embeddings() -> HuggingFaceEmbeddings:
    '''
    Setup the embeddings that we use for vector search
    '''
    global _embeddings

    if (_embeddings == None):
        logging.debug("Setting up Embeddings")

        model_name = config.read("MODEL_TRANSFORMERS")
        logging.debug("Attempting to use embeddings:"+model_name)

        _embeddings = HuggingFaceEmbeddings(model_name=model_name)
    else:
        logging.debug("Embeddings already setup")

    return _embeddings


def _get_setup_llm():

    global _llm_to_use

    if (_llm_to_use == None):

        # we need to set it up accoding to sessings
        MODEL_LLM = config.read("MODEL_LLM")
        logging.debug(f"Attmpting to setup LLM {MODEL_LLM}")


        # check local llama instance running
        # If you get an error from the following line, double check the
        # install at https://github.com/ollama/ollama
        requests.get("http://localhost:11435/")

        if (MODEL_LLM == "llama3.2"):

            try:
                _llm_to_use = OllamaLLM(model="llama3.2", stop=['<|eot_id|>'])
            except ConnectionRefusedError as cre:

                logging.warning("\n\nFailure to setup local Model - check is Ollame running\n\n")
                raise cre


        elif (MODEL_LLM == "google/flan-t5-large"):

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



        elif (MODEL_LLM == "google"):
            logging.debug("Using Google Gemini LLM")


            token = token_loader.setup_token("google")
            secret_token = langchain_core_utils.convert_to_secret_str(token)

 
            _llm_to_use  = ChatGoogleGenerativeAI(
                model="gemini-1.5-pro",
                temperature=0,
                max_tokens=None,
                timeout=None,
                max_retries=2,
                api_key=secret_token
                # other params...
            )



        elif (MODEL_LLM == "claude"):

            logging.debug("Using Claude Anthropic LLM")

            token = token_loader.setup_token("claude")
            secret_token = langchain_core_utils.convert_to_secret_str(token)


            _llm_to_use = ChatAnthropic(
                model_name="claude-3-5-sonnet-20240620",
                api_key=secret_token,
                temperature=0,
                timeout=None,
                stop=None,
                max_retries=2,
                # other params...
            )



        elif (MODEL_LLM == "openai"):
            logging.debug("Using Open AI LLM")

            token = token_loader.setup_token("openai")
            secret_token = langchain_core_utils.convert_to_secret_str(token)


            _llm_to_use = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0, api_key=secret_token)

        elif (MODEL_LLM == "copilot"):
            logging.debug("Using Copilot LLM")
            token = token_loader.setup_token("copilot")
            _llm_to_use = llm_copilot.CopilotLLM(copilot_token=token)

        else:
            logging.debug("Default LLM to Echo (for testing)")
            _llm_to_use = llm_echo.EchoLLM()

    else:

        logging.debug("LLM already setup")

    return _llm_to_use


def _get_setup_knowledgebase_retriever(index_name: str) -> BaseRetriever:
    '''
    Setup Handle to the external RAG Datastore
    '''
    global _knowledgebase_retriever_dict

    #ensure our embeddings are setup
    local_embeddings= _get_setup_vector_embeddings()


    if (index_name not in _knowledgebase_retriever_dict):

        logging.debug("Setting up Elastic Knowledgebase:" +
                      index_name + " using embeddings:"+str(local_embeddings))

        tmpES_Store = ElasticsearchStore(embedding=_embeddings, es_url=config.read(
            "ES_URL"), index_name=index_name, strategy=DenseVectorStrategy()) #was ApproxRetrievalStrategy
        
        #convert to standard langchain retriever format
        _knowledgebase_retriever_dict[index_name] = tmpES_Store.as_retriever(search_type="similarity_score_threshold", search_kwargs={"score_threshold": 0.2})


    else:
        logging.debug("Using cached Datastore "+index_name)

    return _knowledgebase_retriever_dict[index_name]


def get_nearest_match_documents(index_name: str, search_text: str) -> List[Document]:
    '''
    Get the nearest match documents using vector search
    '''

    logging.debug(f"Nearest Search index {index_name} matching against {search_text}")

    # Get the handle to the Elastic Knowledge Base
    vector_retriever = _get_setup_knowledgebase_retriever(index_name)

    return vector_retriever.invoke(search_text)


def get_llm_chain(prompt_template: str) :
    '''
    Generate the LLM Chain
    '''

    local_llm = _get_setup_llm()
    logging.info(f"Configured to use LLM:{local_llm}")

    prompt_informed = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"])
    
    parser = JsonOutputFunctionsParser()
    
    #New Langchain 0.3 syntax
    llm_chain = prompt_informed | local_llm

    return llm_chain
