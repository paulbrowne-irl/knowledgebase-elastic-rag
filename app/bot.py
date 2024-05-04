import logging
import util_file.xl  as xl_rw
import settings.config as config

from templates import prompts as prompts
from util_rag import rag_controller as rag_controller


'''
Bot that uses Rag to respond to emails. It uses a Sharepoint / excel list to mediate emails (i.e. does not read and write them directly)

So it relies on the following ...

* power automate flow to update excel sheet
* excel sheet updated with emails
* power automate flow to email people w

'''

def answer_questions_in_excel():

    # read excel file (filtered)
    question_file_name=config.read("QUESTION_FILE_XLS")

    logging.debug("Reading next question needing answered from "+question_file_name)
    next_question_df = xl_rw.read_next_unanswered_question(question_file_name)
    next_question = next_question_df.to_dict()

    logging.debug("Question we are trying to answer:"+str(next_question.get("Question")))


    #make sure setup gets run at start
    rag_controller.setup()

    # read email and prompt templates
    qa_prompt=prompts.TEMPLATE_EMAIL_PROMPT


    # Find nearest match documents
    name_of_index_to_search= config.read("ES_INDEX_KB")
    similar_docs = rag_controller.get_nearest_match_documents(name_of_index_to_search, str(next_question.get("Question")))
    logging.info("relevant docs:"+str(similar_docs))


    ## Ask Local LLM context informed prompt
    informed_context= similar_docs[0].page_content

    name_of_llm_to_use=config.read("REMOTE_MODEL_LLM")
    logging.debug("Name of LLM being used:"+name_of_llm_to_use)

    llm_chain = rag_controller.get_llm_chain(name_of_llm_to_use, qa_prompt)
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

    #call the main method in this module
    answer_questions_in_excel()

                