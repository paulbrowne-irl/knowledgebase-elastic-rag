import fnmatch
import logging
import traceback

import settings.config as config
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import ElasticVectorSearch
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores.elasticsearch import ElasticsearchStore
from pandas.core.frame import DataFrame
from tqdm import tqdm

'''
Module level setup - should be called only once
'''
text_splitter = CharacterTextSplitter(
    separator="\n\n",
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len,
    is_separator_regex=False,
)

# get the model we need to encode the text as vectors (in Elastic)
print("Prep. Huggingface embedding setup")
hf= HuggingFaceEmbeddings(model_name=settings.MODEL_TRANSFORMERS)




'''
Walk folder recursively
'''
def index_text_and_meta_data(index_name: str,filename: str,filecontents: str) -> None:

    # Next we'll create our elasticsearch vectorstore in the langchain style:
    db = ElasticVectorSearch(embedding=hf,elasticsearch_url=es_url, index_name=settings.ES_INDEX_DOCUMENTS)


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

    db.from_documents(pages, embedding=hf, elasticsearch_url=es_url, index_name=index_name)

    print (f'processed message {counter}')




           
        


# simple code to test from command line
if __name__ == '__main__':
    
    ## Module level variables
    counter=0

    # Get the elastic URL from settings
    # If we can to allow for username and password we can update to something like:
    # es_url =  f"https://{username}:{password}@{endpoint}:9200"
    # noting that the username, assword and endpoint should valid
    es_url =  settings.ES_URL
    print ("Using URL "+settings.ES_URL)

    #Set the Logging level. Change it to logging.INFO is you want just the important info
    logging.basicConfig(filename=settings.LOG_FILE, encoding='utf-8', level=logging.DEBUG)


    #Walk folders
    print("About to walk folder");
    _walk_folder("",root_folder)

    





