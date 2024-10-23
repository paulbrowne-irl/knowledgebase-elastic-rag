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
from lang_server import lc_controller as lc_controller

from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from sentence_transformers import SentenceTransformer



'''
Bot that uses Rag to respond to emails. It uses a Sharepoint / excel list to mediate emails (i.e. does not read and write them directly)

So it relies on the following ...

* power automate flow to update excel sheet
* excel sheet updated with emails
* power automate flow to email people w

'''
class Bot_Excel(bot.Bot):

    #Excel Bot specific confir values
    QUESTION_FILE_NAME=config.read("QUESTION_FILE_XLS")
    COL_QUESTION=config.read("COL_TO_READ_QUESTION_IN_FILE")
    COL_TO_UPDATE_RELEVANT_DOCS=config.read("COL_TO_UPDATE_RELEVANT_DOCS")
    COL_TO_UPDATE_SUGGESTED_ANSWER=config.read("COL_TO_UPDATE_SUGGESTED_ANSWER")
    OUTPUT_FILE = config.read("BOT_OUTPUT_FILE")


    def loop_answer_questions_from_source(self):
    
        '''
        Loop through the specified question file, attempting to answer the question files
        '''

        #setup the loop

        #output data
        output_data = []



        # get the questions needing answer
        logging.debug("Reading questions needing answered from "+self.QUESTION_FILE_NAME)
        unanswered_questions_df = xl_rw.read_unanswered_questions(self.QUESTION_FILE_NAME,self.COL_QUESTION,self.COL_TO_UPDATE_SUGGESTED_ANSWER)
        logging.debug("Number of unanswered questions:"+str(len(unanswered_questions_df.index)))

        # Loop through questions
        for index,next_question in unanswered_questions_df.iterrows():

            logging.info("Next question line:"+str(index))
            logging.info(str(next_question))

            #generate the chain using the prompt
            llm_chain = lc_controller.get_llm_chain(prompts.TEMPLATE_EMAIL_PROMPT)

            logging.debug("Question we are trying to answer:"+str(next_question.get(self.COL_QUESTION)))

            #get the suggested answer and supporting docs
            informed_response, supporting_docs = self._get_suggested_anwser_using_chain(llm_chain,str(next_question.get(self.COL_QUESTION)))

            logging.info("Response:"+informed_response)

            # gather meta data into output
            supporting_doc_text="This answer relies on information from:\n"
            for this_supporting_doc in supporting_docs:
                supporting_doc_text +="DATA_SOURCE:"+str(this_supporting_doc.metadata["DATA_SOURCE"]+ " ")
                supporting_doc_text +="PARENT_FOLDER:"+str(this_supporting_doc.metadata["PARENT_FOLDER"]+ " ")
                supporting_doc_text +="FILE_NAME:"+str(this_supporting_doc.metadata["FILE_NAME"]+ " ")
                supporting_doc_text +="PAGE:"+str(this_supporting_doc.metadata["page"])+ " "
                supporting_doc_text +="\n"


            # save into output
            next_question[self.COL_TO_UPDATE_SUGGESTED_ANSWER]=informed_response
            next_question[self.COL_TO_UPDATE_RELEVANT_DOCS]=supporting_doc_text
            output_data.append(next_question)

            #save output the dataframe
            output_df = pd.DataFrame(output_data)
            output_df.to_excel(self.OUTPUT_FILE)
            logging.info(f"Output to overwrite {self.OUTPUT_FILE} - need to manually update into main sheet")
            
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
    myBot = Bot_Excel()
    myBot.loop_answer_questions_from_source()

