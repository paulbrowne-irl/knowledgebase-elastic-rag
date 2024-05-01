import logging
import util_file.xl  as xl
import settings.config as config

'''
Bot that uses Rag to respond to emails. It uses a Sharepoint / excel list to mediate emails (i.e. does not read and write them directly)

So it relies on the following ...

* power automate flow to update excel sheet
* excel sheet updated with emails
* power automate flow to email people w

'''

#Set the Logging level. Change it to logging.INFO is you want just the important info
#logging.basicConfig(filename=config.read("LOG_FILE"), encoding='utf-8', level=logging.DEBUG)
logging.basicConfig(level=logging.DEBUG)

# read excel file (filtered)
question_file_name=config.read("QUESTION_FILE_XLS")

logging.debug("Reading next question needing answered from "+question_file_name)
next_question_df = xl.read_next_unanswered_question(question_file_name)
next_question = next_question_df.to_dict()

logging.debug("Question we are trying to answer:"+str(next_question.get("Question")))


# read email and prompt templates
qa_prompt=""


# identify unprcessed email

# Loop


    # call via chain

    # upate sheet

    # on to next
