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

from langchain_community.embeddings import HuggingFaceEmbeddings
from sentence_transformers import SentenceTransformer

'''
Bot that uses Rag to respond to emails. It uses a Sharepoint / excel list to mediate emails (i.e. does not read and write them directly)

So it relies on the following ...

* power automate flow to update excel sheet
* excel sheet updated with emails
* power automate flow to email people w

'''

#get config values
ELASTIC_INDEX_NAME= config.read("ES_INDEX_KB")
QUESTION_FILE_NAME=config.read("QUESTION_FILE_XLS")
COL_QUESTION=config.read("COL_TO_READ_QUESTION_IN_FILE")
COL_TO_UPDATE_RELEVANT_DOCS=config.read("COL_TO_UPDATE_RELEVANT_DOCS")
COL_TO_UPDATE_SUGGESTED_ANSWER=config.read("COL_TO_UPDATE_SUGGESTED_ANSWER")
RANDOM_DELAY_RANGE=config.read_int("RANDOM_DELAY_RANGE")

def _get_suggested_anwer(llm_chain:LLMChain,next_question:str)->Tuple[str,List[Document]]:
    '''
    find suggested answer using RAG techique
    '''
    # Find nearest match documents
    similar_docs = rag_controller.get_nearest_match_documents(ELASTIC_INDEX_NAME,next_question)
    logging.info("relevant docs:"+str(similar_docs))

    ## Ask Local LLM context informed prompt
    informed_context= similar_docs[0].page_content

    informed_response = llm_chain.run(context=informed_context,question=next_question)

    return informed_response, similar_docs





def answer_questions_in_excel():
    
    '''
    Loop through the specified question file, attempting to answer the question files
    '''

    #setup the loop

    #output data
    output_data = []

    #for testing only
    #rag_controller._llm_to_use = llm_echo.EchoLLM()



    # get the questions needing answer
    logging.debug("Reading questions needing answered from "+QUESTION_FILE_NAME)
    unanswered_questions_df = xl_rw.read_unanswered_questions(QUESTION_FILE_NAME,COL_QUESTION,COL_TO_UPDATE_SUGGESTED_ANSWER)
    logging.debug("Number of unanswered questions:"+str(len(unanswered_questions_df.index)))

    # Loop through questions
    for index,next_question in unanswered_questions_df.iterrows():

        #generate the chain using the prompt
        llm_chain = rag_controller.get_llm_chain(prompts.TEMPLATE_EMAIL_PROMPT)
       
        logging.info("Next question line:"+str(index))
        logging.info(str(next_question))

        logging.debug("Question we are trying to answer:"+str(next_question.get(COL_QUESTION)))

        #get the suggested answer and supporting docs
        informed_response, supporting_docs = _get_suggested_anwer(llm_chain,str(next_question.get(COL_QUESTION)))

        logging.info("Response:"+informed_response)

        # gather meta data into output
        supporting_doc_text="This answer relies on information from:"
        for this_supporting_doc in supporting_docs:
            supporting_doc_text +=str(this_supporting_doc.metadata)

        # save into output
        next_question[COL_TO_UPDATE_SUGGESTED_ANSWER]=informed_response
        next_question[COL_TO_UPDATE_RELEVANT_DOCS]=supporting_doc_text
        output_data.append(next_question)
        
        # wait random amount of time to allow sync, avoid spam copilot
        wait_random = randint(1,RANDOM_DELAY_RANGE)
        logging.info("Waiting random seconds:"+str(wait_random))
        sleep(wait_random)

    #save output the dataframe
    output_df = pd.DataFrame(output_data)
    output_df.to_excel("output.xlsx")

    logging.info("Output to output.xlsx - need to manually update into main sheet ")




# simple code to run from command line
if __name__ == '__main__':
    #Set the Logging level. Change it to logging.INFO is you want just the important info
    #logging.basicConfig(filename=config.read("LOG_FILE"), encoding='utf-8', level=logging.DEBUG)
    logging.basicConfig(level=logging.DEBUG)


    #make sure setup gets run at start
    rag_controller.setup()

    #call the main method in this module
    answer_questions_in_excel()

                