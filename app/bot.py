import logging
import pickle

from shareplum import Site
from shareplum import Office365
from shareplum.site import Version

from office365.sharepoint.client_context import ClientContext
from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.user_credential import UserCredential

'''
Bot that uses Rag to respond to emails.

It uses a Sharepoint list to mediate emails (i.e. does not read and write them directly)

So it relies on the following

* sharepoint list (spec)

'''

token =""


def _setup_sharepilot_token(): 
   
    global token
 
    try:
        token = pickle.load(open("token-sharepoint.pickle", "rb"))
        print ("Loaded sharepoint token from pickle file")

    except Exception:
        token = input("Please enter the Sharepoint token. This will be saved in token-sharepoint.pickle.   ")
        pickle.dump(token, open("token-sharepoint.pickle", "wb"))


# simple code to run from command line
if __name__ == '__main__':

       _setup_sharepilot_token() 

