import logging
import traceback
from pandas.core.frame import DataFrame


import pandas as pd


import settings.config as config


from tqdm import tqdm
from langchain.embeddings import HuggingFaceEmbeddings


from langchain.vectorstores import ElasticVectorSearch
from langchain_community.vectorstores.elasticsearch import ElasticsearchStore
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter

import fnmatch


'''
Index Mails (stored in Excel Sheet) to Elastic stack
'''



'''
Walk folder recursively
'''
def _loop_over_file(mail_df):

    #handle to variables
    global counter
    
    text_splitter = CharacterTextSplitter(
    separator="\n\n",
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len,
    is_separator_regex=False,
    )

    for index, row in mail_df.iterrows():
        logging.debug(index,row)

        try:
            #Increment the counter and test if we need to break
            counter+=1


            ## Split our mail body into pages
            pages = text_splitter.create_documents([str(row['Body'])])


            # Adding metadata to each of these document / pages
            for i, doc in enumerate(pages):
                doc.metadata['Parent']=str(row['Parent'])
                doc.metadata['Subject']=str(row['Subject'])
                doc.metadata['To']=str(row['To'])
                doc.metadata['CC']=str(row['CC'])
                doc.metadata['Recipients']=str(row['Recipients'])
                doc.metadata['RecievedByName']=str(row['RecievedByName'])
                doc.metadata['ConversationTopic']=str(row['ConversationTopic'])
                doc.metadata['ConversationID']=str(row['ConversationID'])
                doc.metadata['Sender']=str(row['Sender'])
                doc.metadata['SenderName']=str(row['SenderName'])
                doc.metadata['SenderEmailAddress']=str(row['SenderEmailAddress'])
                doc.metadata['attachments.Count']=str(row['attachments.Count'])
                doc.metadata['Size']=str(row['Size'])
                doc.metadata['ConversationIndex']=str(row['ConversationIndex'])
                doc.metadata['EntryID']=str(row['EntryID'])
                doc.metadata['Parent']=str(row['Parent'])
                doc.metadata['CreationTime']=str(row['CreationTime'])
                doc.metadata['ReceivedTime']=str(row['ReceivedTime'])
                doc.metadata['LastModificationTime']=str(row['LastModificationTime'])
                doc.metadata['Categories']=str(row['Categories'])
                
                doc.metadata["product"] = "UECS"
                doc.metadata["format"] = "Mail"
                doc.metadata["type"] = "Inquiry"

            db.from_documents(pages, embedding=hf, elasticsearch_url=es_url, index_name=config.read("ES_INDEX_EMAILS"))

            print (f'processed message {index}')


        except Exception as e:
            logging.debug("error when processing item - will continue")
            logging.debug(e)

    


           
        


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
    logging.debug("Prep. Huggingface embedding setup")
    hf= HuggingFaceEmbeddings(model_name=config.read("LOCAL_MODEL_TRANSFORMERS"))

    # Next we'll create our elasticsearch vectorstore in the langchain style:
    db = ElasticVectorSearch(embedding=hf,elasticsearch_url=es_url, index_name=config.read("ES_INDEX_KB"))

    #Set the Logging level. Change it to logging.INFO is you want just the important info
    logging.basicConfig(filename=config.read("LOG_FILE"), encoding='utf-8', level=logging.DEBUG)

    #root_folder = .Folders.Item(1)
    logging.debug("Getting handle to Excel with Emails");
    email_table = pd.read_excel(config.read("SOURCE_MAILS_IN_XL"), index_col=0) 

    #Walk folders
    logging.debug("About to loop through emails ");
    _loop_over_file(email_table)

    





