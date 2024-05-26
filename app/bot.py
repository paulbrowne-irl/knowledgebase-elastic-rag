import logging

from app.util.rag import llm_echo
import settings.config as config
from templates import prompts as prompts
from util.office import xl_rw as xl_rw
from util.rag import rag_controller as rag_controller

'''
Bot that uses Rag to respond to emails. It uses a Sharepoint / excel list to mediate emails (i.e. does not read and write them directly)

So it relies on the following ...

* power automate flow to update excel sheet
* excel sheet updated with emails
* power automate flow to email people w

'''

#get config values
QUESTION_FILE_NAME=config.read("QUESTION_FILE_XLS")
COL_TO_READ_QUESTION_IN_FILE=config.read("COL_TO_READ_QUESTION_IN_FILE")
COL_TO_UPDATE_RELEVANT_DOCS=config.read("COL_TO_UPDATE_RELEVANT_DOCS")
COL_TO_UPDATE_SUGGESTED_ANSWER=config.read("COL_TO_UPDATE_SUGGESTED_ANSWER")

def answer_questions_in_excel():
    '''
    Loop through the specified question file, attempting to answer the question files
    '''

    # read excel file (filtered)

    logging.debug("Reading next question needing answered from "+QUESTION_FILE_NAME)
    next_question_df = xl_rw.read_next_unanswered_question(QUESTION_FILE_NAME)
    next_question = next_question_df.to_dict()

    logging.debug("Question we are trying to answer:"+str(next_question.get("Question")))



    # read email and prompt templates
    qa_prompt=prompts.TEMPLATE_EMAIL_PROMPT


    # Find nearest match documents
    name_of_index_to_search= config.read("ES_INDEX_KB")
    similar_docs = rag_controller.get_nearest_match_documents(name_of_index_to_search, str(next_question.get("Question")))
    logging.info("relevant docs:"+str(similar_docs))


    ## Ask Local LLM context informed prompt
    informed_context= similar_docs[0].page_content

    #for testing only
    rag_controller._llm_to_use = llm_echo.EchoLLM()

    #generate the chain using the prompt
    llm_chain = rag_controller.get_llm_chain(qa_prompt)
    informed_response = llm_chain.run(context=informed_context,question=str(next_question.get("Question")))

    logging.info("Response:"+informed_response)

    # save into excel
        # response
        # themes
        # relevant docs



    # identify unprcessed email

    # Loop


        # call via chain

        # upate sheet

        # on to next



# simple code to run from command line
if __name__ == '__main__':
    #Set the Logging level. Change it to logging.INFO is you want just the important info
    #logging.basicConfig(filename=config.read("LOG_FILE"), encoding='utf-8', level=logging.DEBUG)
    logging.basicConfig(level=logging.DEBUG)

    #make sure setup gets run at start
    rag_controller.setup()

    #call the main method in this module
    answer_questions_in_excel()

                