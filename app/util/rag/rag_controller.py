import logging
import os
import getpass
from typing import (Any, Callable, Dict, Iterable, List, Literal, Optional,
                    Tuple, Union)

import settings.config as config
import settings.token_loader as token_loader
import util.rag.llm_copilot as llm_copilot
from langchain.chains.llm import LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import HuggingFacePipeline, Ollama
from langchain_core.documents import Document
from langchain_elasticsearch import ApproxRetrievalStrategy, ElasticsearchStore
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline
from util.rag import llm_echo

from langchain_core.retrievers import BaseRetriever

#from langchain_core.messages import HumanMessage, SystemMessage
#from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
#from langchain_google_vertexai import ChatVertexAI
from langchain_anthropic import ChatAnthropic


# Module level constants
_embeddings = None
_kb_dict = {}
_llm_to_use = None


def setup():
    '''
    Initialise the system (if needed)
    Safe to call multiple types as checks if have been called prviously
    '''
    _setup_vector_embeddings()
    _setup_llm()


def _setup_vector_embeddings():
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


def _setup_llm():

    global _llm_to_use
    global _embeddings

    if (_llm_to_use == None):

        # we need to set it up accoding to sessings
        MODEL_LLM = config.read("MODEL_LLM")
        logging.debug(f"Attmpting to setup LLM {MODEL_LLM}")

        if (MODEL_LLM == "llama3"):
            _llm_to_use = Ollama(model="llama3", stop=['<|eot_id|>'])

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
            logging.debug("Using Gemini LLM")

            token = token_loader.setup_token("google")

            _llm_to_use = ChatGoogleGenerativeAI(
                model="gemini-1.0-pro", api_key=token)  # was gemini-pro



        elif (MODEL_LLM == "claude"):

            logging.debug("Using Anthropic LLM")

            token = token_loader.setup_token("claude")

            _llm_to_use = ChatAnthropic(
                temperature=0, api_key=token, model_name="claude-3-opus-20240229")



        elif (MODEL_LLM == "openai"):
            logging.debug("Using Open AI LLM")

            token = token_loader.setup_token("openai")

            _llm_to_use = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0, api_key=token)

        elif (MODEL_LLM == "copilot"):
            logging.debug("Using Copilot LLM")
            token = token_loader.setup_token("copilot")
            _llm_to_use = llm_copilot.CopilotLLM(copilot_token=token)

        else:
            logging.debug("Default LLM to Echo (for testing)")
            _llm_to_use = llm_echo.EchoLLM()

    else:

        logging.debug("LLM already setup")


def _get_knowledgebase_retriever(index_name: str) -> BaseRetriever:
    '''
    Setup Handle to the external RAG Datastore
    '''

    if (index_name not in _kb_dict):

        logging.debug("Setting up Elastic Knowledgebase:" +
                      index_name + " using embeddings:"+str(_embeddings))

        tmpES_Store = ElasticsearchStore(embedding=_embeddings, es_url=config.read(
            "ES_URL"), index_name=index_name, strategy=ApproxRetrievalStrategy())
        
        ## testing if we can do this - from https://python.langchain.com/docs/integrations/vectorstores/elasticsearch/
        print("#### Start test")
        _kb_dict[index_name] = tmpES_Store.as_retriever(search_type="similarity_score_threshold", search_kwargs={"score_threshold": 0.2})
        print("#### success!!")


    else:
        logging.debug("Using cached Datastore "+index_name)

    return _kb_dict[index_name]


def get_nearest_match_documents(index_name: str, vector_search_text: str) -> List[Document]:
    '''
    Get the nearest match documents using vector search
    '''

    logging.debug(f"Nearest Search index {index_name} matching against {vector_search_text}")

    # Get the handle to the Elastick Knowledge Base
    vector_retriever = _get_knowledgebase_retriever(index_name)

    return vector_retriever.invoke(vector_search_text)


def get_llm_chain(prompt_template: str) -> LLMChain:
    '''
    Generate the LLM Chain
    '''

    global _llm_to_use
    logging.info(f"Configured to use LLM:{_llm_to_use}")

    prompt_informed = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"])
    
    llm_chain = LLMChain(prompt=prompt_informed, llm=_llm_to_use)

    return llm_chain
