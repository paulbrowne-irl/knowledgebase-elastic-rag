'''
Simple rest client for interacting with API
'''
import logging
import requests
import settings.config as config


def call_rest_to_get_email_draft(prompt_email:str) -> str:
    '''
    Call the API Server to draft the email
    prompt_email - that we pass to the LLM for a response
    use_cache - skip the LLM , use a previously cached result
    '''


    END_POINT = config.read("DRAFT_EMAIL_END_POINT")
    logging.info(f"Using Endpoint {END_POINT}")

    payload = {'email': prompt_email}

    resp = requests.get(END_POINT, params=payload)
    
    logging.debug(f"Server returned response code:{resp.status_code}")
    
    try:
        resp_json= resp.json()
        returnvalue = resp_json["suggested_text"]
    except:
        returnvalue = resp.text

    return returnvalue


'''
Simple test to run from the command line (in app folder)
python -m pages.support.rest_client
'''
if __name__ == '__main__':

    print("Start")

    #setup logging
    # logger = logging.getLogger("")
    # logger.setLevel(logging.DEBUG)
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True

    logging.info("\n")
    logging.info(call_rest_to_get_email_draft("Is it getting better, or do you feel the same?"))
    logging.info("\nComplete")