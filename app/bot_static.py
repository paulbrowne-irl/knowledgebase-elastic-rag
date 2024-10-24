import logging
from random import randint
from time import sleep
from typing import (Any, Callable, Dict, Iterable, List, Literal, Optional,
                    Tuple, Union)

import util.bot as bot
import pandas as pd
import settings.config as config
from service import rag_factory as rag_factory
from langchain.chains.llm import LLMChain
from langchain_core.documents import Document
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from sentence_transformers import SentenceTransformer
from templates import prompts as prompts
from util.office import xl_rw as xl_rw

'''
Not really a bot - more of a test bed.

uses Hardcoded values to do ask questions of the Bot's RAG implementation

'''
class Bot_Static(bot.Bot):

    #setup the loop
    input_questions=[
        "What foods should you eat while in Dublin?",
        "Should I go to college to study accounting?"
    ]

    
    #output data
    output_data = []

    '''
    ######################################
    '''
    def _use_new_chain_refactor(self,next_question):
      
        messages = [
            SystemMessage(content=next_question),
            HumanMessage(content="hi!"),
        ]

        ## refactor to use later
        retriever = rag_factory._get_setup_knowledgebase_retriever(self.ELASTIC_INDEX_NAME)

        ##model start
        model = rag_factory._get_setup_llm() # also returns llm

        ## end

        

        parser = StrOutputParser()

        chain = retriever | model | parser

        logging.info("About to invoke chain - this may take several seconds if local")
        result = chain.invoke(messages)

        return result


    '''
    ######################################
    '''
    def loop_answer_questions_from_source(self):
    
        '''
        Loop through the specified question list, attempting to answer the question files
        '''

        # Loop through questions
        for next_question in self.input_questions:

            logging.info("Next question line:"+str(next_question))

            #generate the chain using the prompt
            llm_chain = rag_factory.get_llm_chain(prompts.TEMPLATE_EMAIL_PROMPT)

            #get the suggested answer and supporting docs
            #informed_response, supporting_docs = self._get_suggested_anwser_using_chain(llm_chain,next_question)
            informed_response = self._use_new_chain_refactor(next_question)


            logging.info("Response:"+informed_response)

            self.output_data.append(informed_response)

            # wait random amount of time to allow sync, avoid spam llm
            wait_random = randint(1,self.RANDOM_DELAY_RANGE)
            logging.info("Waiting random seconds:"+str(wait_random))
            sleep(wait_random)





# simple code to run from command line
if __name__ == '__main__':
    #Set the Logging level. Change it to logging.INFO is you want just the important info
    #logging.basicConfig(filename=config.read("LOG_FILE"), encoding='utf-8', level=logging.DEBUG)
    logging.basicConfig(level=logging.DEBUG)

    #call the main method in this module
    myBot = Bot_Static()
    myBot.loop_answer_questions_from_source()

