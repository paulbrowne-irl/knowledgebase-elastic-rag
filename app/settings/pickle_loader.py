import pickle

'''
Helper class to get / set confidential values in pickle
'''

def setup_sharepilot_token(): 
   
    global token
 
    try:
        token = pickle.load(open("token-sharepoint.pickle", "rb"))
        print ("Loaded sharepoint token from pickle file")

    except Exception:
        token = input("Please enter the Sharepoint token. This will be saved in token-sharepoint.pickle.   ")
        pickle.dump(token, open("token-sharepoint.pickle", "wb"))