import requests
import logging
import pprint as pprint


''''
Proxy help methods to invoke the chain (via simple server)
'''
SERVICE_BASE="http://localhost:8000/"
SERVICE_CHECK_URL=SERVICE_BASE+"service_check"
SERVICE_DRAFT_EMAIL=SERVICE_BASE+"draft_email_response"


def do_server_check(url:str=SERVICE_CHECK_URL):
    '''
    Checks if the configured server gives a response, else starts local server
    '''
    try:
        requests.get(url)
        logging.info("Local server detected")
    except:
        # nothing there
        logging.warning("\n\nNo server detected - perhaps you need to start the server    uvicorn service.service_email:app --reload?\n\n")


def proxy_draft_email() -> str:
    '''
    Get a Langchain driven AI response to our question
    '''
    
    # from https://realpython.com/api-integration-in-python/
    # https://www.datacamp.com/tutorial/making-http-requests-in-python
    # https://requests.readthedocs.io/en/latest/


    #TODO - refactor into config
    #TODO - refactor into true client

    # check service is running
    do_server_check()


    new_data = {
        "email": "this is some sample text that an email would be",
        "query": "query"
    }

    # A GET request to the API
    response = requests.post(SERVICE_DRAFT_EMAIL,params=new_data)
    print(response)

    # Print the response
    response_json = response.json()
    print(response_json)

    
    return response_json




'''
# simple code to run from command line

To run this code in test mode - from within the app folder
python3 -m util.simple_proxy
'''
if __name__ == '__main__':
    
    #Set the Logging level. Change it to logging.INFO is you want just the important info
    #logging.basicConfig(filename=config.read("LOG_FILE"), encoding='utf-8', level=logging.DEBUG)
    logging.basicConfig(level=logging.INFO)
    
    proxy_draft_email()
    

