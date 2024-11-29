import json
import logging
import os

TOKEN_STORAGE_1 = "settings/token-storage-local.json"
TOKEN_STORAGE_2 ="app/settings/token-storage-local.json"

'''
Helper class to get / set confidential values in JSON
Note the token may be set as clear text in the (local) JSON file - be sure to secure
'''

def setup_token(token_name:str)->str: 
    '''
    see if user has set token, other request and store it    
    '''
    
    json_storage_file=TOKEN_STORAGE_1

    if(not os.path.isfile(json_storage_file)):
        json_storage_file = TOKEN_STORAGE_2

    output_token=""
    token_data={}

    try:
        # open json file in a way that automatically closes
        with open(json_storage_file) as token_file:

            token_data = json.load(token_file)
            output_token = token_data[token_name]

            logging.info (f"Loaded {token_name} token from json file")

    except Exception:
        
        logging.debug("Could not find previous token in: "+json_storage_file)
        token = input(f"Please enter the {token_name} token. This will be saved locally in token-storage-local.json:   ")
        token_data[token_name]=token
        output_token=token

    # make sure we save all our values
    with open(json_storage_file,"w") as token_file:
        json.dump(token_data,token_file)

    return output_token




# simple code to run from command line and generate
if __name__ == '__main__':
    setup_token("TEST2")
