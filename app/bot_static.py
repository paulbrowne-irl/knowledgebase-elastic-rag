import logging
from service import rag_factory as rag_factory
from templates import prompts as prompts
from util.office import xl_rw as xl_rw

'''
Not really a bot - more of a test bed.

uses Hardcoded values to do ask questions of the Bot's RAG implementation

'''
class Bot_Static():

    #setup the loop
    input_questions=[
        "What foods should you eat while in Dublin?",
        "Should I go to college to study accounting?"
    ]

    
    #output data
    output_data = []


    '''
    Loop and answer quetions from the source
    '''
    def loop_answer_questions_from_source(self):
    
        '''
        Loop through the specified question list, attempting to answer the question files
        '''

        # Loop through questions
        for next_question in self.input_questions:

            logging.info("Next question line:"+str(next_question))

            #call the service directly / via the proxy
            logging.info("Calling Service to get answer")
            # TODO
            informed_response = "TBD"


            logging.info("Response:"+informed_response)

            self.output_data.append(informed_response)





# simple code to run from command line
if __name__ == '__main__':
    #Set the Logging level. Change it to logging.INFO is you want just the important info
    #logging.basicConfig(filename=config.read("LOG_FILE"), encoding='utf-8', level=logging.DEBUG)
    logging.basicConfig(level=logging.DEBUG)

    #call the main method in this module
    myBot = Bot_Static()
    myBot.loop_answer_questions_from_source()

