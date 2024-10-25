from langserve import RemoteRunnable 
import requests
import logging


''''
Proxy help methods to invoke the chain (via proper server)
'''

#Set the Logging level. Change it to logging.INFO is you want just the important info
#logging.basicConfig(filename=config.read("LOG_FILE"), encoding='utf-8', level=logging.DEBUG)
logging.basicConfig(level=logging.INFO)

def do_server_check(url:str):
    '''
    Checks if the configured server gives a response, else starts local server
    '''
    try:
        requests.get(url)
        logging.info("Local server detected")
    except:
        # nothing there
        logging.info("No server detected - perhaps you need to start simple_server.py?")


def get_response() -> str:
    '''
    Get a Langchain driven AI response to our question
    '''

    url = "http://localhost:8000/draft_email/"

    do_server_check(url)


    # Data to be sent
    data = {
        "input_email": "Please answer my email question"
    }

    # A POST request to the API
    response = requests.post(url, json=data)

    # Print the response
    print(response.json())

    
    return response


# simple code to run from command line
if __name__ == '__main__':

    

    print(get_response())