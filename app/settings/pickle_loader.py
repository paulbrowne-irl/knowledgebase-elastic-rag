import pickle
import logging

PICKLE_STORAGE_DIR = "settings/"

'''
Helper class to get / set confidential values in pickle
'''

def setup_copilot_token(): 
 
    try:
        token = pickle.load(open(PICKLE_STORAGE_DIR+"token-copilot.pickle", "rb"))
        print ("Loaded copilot token from pickle file")

    except Exception:
        
        logging.debug("Could not find previous token in: "+PICKLE_STORAGE_DIR+"token-copilot.pickle")

        print("Details on how to find your Copilot token are at this page https://github.com/vsakkas/sydney.py")
        token = input("Please enter the Copilot token. This will be saved in token-copilot.pickle")
        pickle.dump(token, open(PICKLE_STORAGE_DIR+"token-copilot.pickle", "wb"))

    return token

# simple code to run from command line and generate
if __name__ == '__main__':
    setup_copilot_token()