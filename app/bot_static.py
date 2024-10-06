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

import bot



'''
Not really a bot - more of a test bed.

uses Hardcoded values to do ask questions of the Bot's RAG implementation

'''
class Bot_Static(bot.Bot):


    def loop_answer_questions_from_source(self):
    
        '''
        Loop through the specified question list, attempting to answer the question files
        '''

        #setup the loop
        input_questions=[
            "question1",
            "question2"
        ]

        #output data
        output_data = []



        # Loop through questions
        for next_question in input_questions:

            logging.info("Next question line:"+str(next_question))

            #generate the chain using the prompt
            llm_chain = rag_controller.get_llm_chain(prompts.TEMPLATE_EMAIL_PROMPT)

            #get the suggested answer and supporting docs
            informed_response, supporting_docs = self._get_suggested_anwser_using_chain(llm_chain,next_question)

            logging.info("Response:"+informed_response)

            output_data.append(informed_response)

            # wait random amount of time to allow sync, avoid spam llm
            wait_random = randint(1,self.RANDOM_DELAY_RANGE)
            logging.info("Waiting random seconds:"+str(wait_random))
            sleep(wait_random)




# simple code to run from command line
if __name__ == '__main__':
    #Set the Logging level. Change it to logging.INFO is you want just the important info
    #logging.basicConfig(filename=config.read("LOG_FILE"), encoding='utf-8', level=logging.DEBUG)
    logging.basicConfig(level=logging.DEBUG)

    #make sure setup gets run at start
    rag_controller.setup()

    #call the main method in this module
    myBot = Bot_Static()
    myBot.loop_answer_questions_from_source()

