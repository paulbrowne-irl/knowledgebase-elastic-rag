from langserve import RemoteRunnable 
import requests

import logging
''''
Proxy help methods to invoke the chain (via proper server)
*OR* Direct local call in not available
'''

#Set the Logging level. Change it to logging.INFO is you want just the important info
#logging.basicConfig(filename=config.read("LOG_FILE"), encoding='utf-8', level=logging.DEBUG)
logging.basicConfig(level=logging.INFO)

def do_server_check():
    '''
    Checks if the configured server gives a response, else starts local server
    '''
    try:
        requests.get("http://localhost:8000/")
        logging.info("Langserve server detected")
    except:
        # nothing there
        logging.info("No server detected - perhaps you need to start simple_server.py?")


def get_response() -> str:
    '''
    Get a Langchain driven AI response to our question
    '''

    do_server_check()

    chain_endpoint = "http://localhost:8000/"
    chain = RemoteRunnable(chain_endpoint)
    response = chain.invoke({"draft_email":"Tell me a joke about Dublin with a bus and a train"})

    return response


# simple code to run from command line
if __name__ == '__main__':

    

    print(get_response())