import logging
import traceback
from pandas.core.frame import DataFrame


import win32com.client


import app.settings.config as config


from tqdm import tqdm
from langchain.embeddings import HuggingFaceEmbeddings


from langchain.vectorstores import ElasticVectorSearch
from langchain_community.vectorstores.elasticsearch import ElasticsearchStore
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter

import fnmatch


'''
Index specified Mailbox to Elastic stack
'''



'''
Walk folder recursively
'''
def _walk_folder(parent_folder,this_folder):

    #handle to variables
    global counter
    
    text_splitter = CharacterTextSplitter(
    separator="\n\n",
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len,
    is_separator_regex=False,
    )
    
    
    # Walk and print folders
    for folder in this_folder.Folders:
        print (folder.Name)
        
        #Do recursive call to walk sub folder
        data_frame = _walk_folder(parent_folder+"::"+folder.Name,folder)

    #Print folder items
    folderItems = this_folder.Items
 
    for mail in folderItems:

        try:
            #Increment the counter and test if we need to break
            counter+=1

            print("Counter:"+str(counter))
            if(config.read_int("BREAK_AFTER_X_MAILS")>0 and counter>config.read_int("BREAK_AFTER_X_MAILS")):
                print("Breaking ...")
                return data_frame
            


            #Filter on mail items only
            if(mail.Class!=43):
                print("Skipping item type:"+str(mail.Class))

            else:


                ## Split our mail body into pages

                pages = text_splitter.create_documents([str(mail.Body)])


                # Adding metadata to each of these document / pages
                for i, doc in enumerate(pages):
                    doc.metadata['Parent']=parent_folder
                    doc.metadata['Subject']=str(mail.Subject)
                    doc.metadata['To']=str(mail.To)
                    doc.metadata['CC']=str(mail.CC)
                    doc.metadata['Recipients']=str(mail.Recipients)
                    doc.metadata['RecievedByName']=str(mail.ReceivedByName)
                    doc.metadata['ConversationTopic']=str(mail.ConversationTopic)
                    doc.metadata['ConversationID']=str(mail.ConversationID)
                    doc.metadata['Sender']=str(mail.Sender)
                    doc.metadata['SenderName']=str(mail.SenderName)
                    doc.metadata['SenderEmailAddress']=str(mail.SenderEmailAddress)
                    doc.metadata['attachments.Count']=str(mail.attachments.Count)
                    doc.metadata['Size']=str(mail.Size)
                    doc.metadata['ConversationIndex']=str(mail.ConversationIndex)
                    doc.metadata['EntryID']=str(mail.EntryID)
                    doc.metadata['Parent']=str(mail.Parent)
                    doc.metadata['CreationTime']=str(mail.CreationTime)
                    doc.metadata['ReceivedTime']=str(mail.ReceivedTime)
                    doc.metadata['LastModificationTime']=str(mail.LastModificationTime)
                    doc.metadata['Categories']=str(mail.Categories)
                   
                    doc.metadata["product"] = "UECS"
                    doc.metadata["format"] = "Mail"
                    doc.metadata["type"] = "Inquiry"

                db.from_documents(pages, embedding=hf, elasticsearch_url=es_url, index_name=config.read("ES_INDEX_EMAILS"))

                print (f'processed message {counter}')


        except Exception as e:
            print("error when processing item - will continue")
            print(e)

            
            #HTMLBody
            #RTFBody


           
        


# simple code to run from command line
if __name__ == '__main__':
    
    ## Module level variables
    counter=0

    # Get the elastic URL from settings
    # If we can to allow for username and password we can update to something like:
    # es_url =  f"https://{username}:{password}@{endpoint}:9200"
    # noting that the username, assword and endpoint should valid
    es_url =  config.read("ES_URL")
    print ("Using URL "+config.read("ES_URL"))

    # get the model we need to encode the text as vectors (in Elastic)
    print("Prep. Huggingface embedding setup")
    hf= HuggingFaceEmbeddings(model_name=config.read("MODEL_TRANSFORMERS"))

    # Next we'll create our elasticsearch vectorstore in the langchain style:
    db = ElasticVectorSearch(embedding=hf,elasticsearch_url=es_url, index_name=config.read("ES_INDEX_DOCUMENTS"))

    #Handle TO Outlook, Logs and other objects we will need later
    OUTLOOK = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

    #Set the Logging level. Change it to logging.INFO is you want just the important info
    logging.basicConfig(filename=config.read("LOG_FILE"), encoding='utf-8', level=logging.DEBUG)

    #root_folder = .Folders.Item(1)
    print("Getting handle to outlook");
    root_folder = OUTLOOK.Folders.Item(config.read("INBOX_NAME"))

    #Walk folders
    print("About to walk folder")
    _walk_folder("",root_folder)

    





