from langserve import RemoteRunnable 
import requests

import lang_server.server as server
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
        requests.get("http://localhost:8001/")
        logging.info("Langserve server detected")
    except:
        # nothing there
        logging.info("no server detected - starting local")
        server.start()

def get_response() -> str:
    '''
    Get a Langchain driven AI response to our question
    '''

    do_server_check()

    chain_endpoint = "http://localhost:8001/"
    chain = RemoteRunnable(chain_endpoint)
    response = chain.invoke({"topic":"Tell me a joke about Dublin"})

    return response


# simple code to run from command line
if __name__ == '__main__':

    

    print(get_response())