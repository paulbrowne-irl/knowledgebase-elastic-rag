import pickle

PICKLE_STORAGE_DIR = "app/settings/"

'''
Helper class to get / set confidential values in pickle
'''

def setup_copilot_token(): 
 
    try:
        token = pickle.load(open(PICKLE_STORAGE_DIR+"token-copilot.pickle", "rb"))
        print ("Loaded sharepoint token from pickle file")

    except Exception:
        token = input("Please enter the Sharepoint token. This will be saved in token-sharepoint.pickle.   ")
        pickle.dump(token, open(PICKLE_STORAGE_DIR+"token-copilot.pickle", "wb"))

    return token

# simple code to run from command line and generate
if __name__ == '__main__':
    setup_copilot_token()