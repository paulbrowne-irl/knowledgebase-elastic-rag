import logging
from random import randint
from time import sleep
from typing import (Any, Callable, Dict, Iterable, List, Literal, Optional,
                    Tuple, Union)

import pandas as pd
import settings.config as config
from langchain.chains.llm import LLMChain
from langchain_core.documents import Document
from templates import prompts as prompts
from util.office import xl_rw as xl_rw
from util.rag import llm_echo
from util.rag import rag_controller as rag_controller

from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from sentence_transformers import SentenceTransformer

from abc import ABC, abstractmethod

'''
Bot that uses Rag to respond to emails. It uses a Sharepoint / excel list to mediate emails (i.e. does not read and write them directly)

So it relies on the following ...

* power automate flow to update excel sheet
* excel sheet updated with emails
* power automate flow to email people w

'''
class Bot(ABC):

    #get config values
    ELASTIC_INDEX_NAME= config.read("ES_INDEX_KB")
    RANDOM_DELAY_RANGE=config.read_int("RANDOM_DELAY_RANGE")



    def _get_suggested_anwser_using_chain(self,llm_chain:LLMChain,this_question:str)->Tuple[str,List[Document]]:
        '''
        Common to all bots - find suggested answer using presetup chain (normally RAG)
        '''
        # Find nearest match documents
        similar_docs = rag_controller.get_nearest_match_documents(Bot.ELASTIC_INDEX_NAME,this_question)
        logging.info("relevant docs:"+str(similar_docs))

        ## Ask Local LLM context informed prompt
        informed_context= similar_docs[0].page_content

        informed_response = llm_chain.run(context=informed_context,question=this_question)
        

        return informed_response, similar_docs

    @abstractmethod
    def loop_answer_questions_from_source(self):
        pass









                