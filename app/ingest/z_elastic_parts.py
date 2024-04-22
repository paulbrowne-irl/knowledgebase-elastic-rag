# Imports
# Make sure the requirements are installed using pip install -r requirements.txt


from tqdm import tqdm
from langchain.embeddings import HuggingFaceEmbeddings

from getpass import getpass
from pathlib import Path
from langchain.vectorstores import ElasticVectorSearch
from langchain_community.vectorstores.elasticsearch import ElasticsearchStore
from langchain_community.document_loaders import PyPDFLoader

from pathlib import Path

import os
import fnmatch

import settings


# Index pdf data into elastic index

# Get the elastic URL from settings
# If we can to allow for username and password we can update to something like:
# es_url =  f"https://{username}:{password}@{endpoint}:9200"
# noting that the username, assword and endpoint should valid
es_url =  settings.ES_URL
print ("Using URL "+settings.ES_URL)

# get the model we need to encode the text as vectors (in Elastic)
print("Prep. Huggingface embedding setup")
hf= HuggingFaceEmbeddings(model_name=settings.MODEL_TRANSFORMERS)

# Next we'll create our elasticsearch vectorstore in the langchain style:
db = ElasticVectorSearch(embedding=hf,elasticsearch_url=es_url, index_name=settings.ES_INDEX_DOCUMENTS)
#db = ElasticsearchStore(es_url,hf,index_name=settings.ES_INDEX)



## get list of files in directory
listFiles = os.listdir(settings.SOURCE_PDF_DIR)

#filter to pdf
listFiles=fnmatch.filter(listFiles, '*.pdf')



for file in listFiles :
    path = settings.SOURCE_PDF_DIR + "/" + file
    print("====== \n")
    print(path)

    ## OLDER
    #line = util.extract_pdf.readPDF(path)
    #eModel = util.extract_pdf.prepareElasticModel(line, file)
    
    ## LANGCHAIN
    loader = PyPDFLoader(path)
    pages = loader.load_and_split()

    # Adding metadata to documents
    for i, doc in enumerate(pages):
        doc.metadata["modified"] = os.path.getmtime(path) 
        doc.metadata["name"] = file
        doc.metadata["product"] = "SEF"
        doc.metadata["format"] = "PDF"
        doc.metadata["type"] = "Application"
        



    ## json method
    '''	
    print("Name : " + str(eModel))

    url = "http://localhost:9200/" + settings.ES_INDEX +"/_doc?pretty"
    data = eModel.toJSON()
    
    response = requests.post(url, data=data,headers={
                    'Content-Type':'application/json',
                    'Accept-Language':'en'

                })
    print("Url : " + url)
    print("Data : " + str(data))

    print("Request : " + str(requests))
    print("Response : " + str(response))
    '''

    #print("ES Indexing:"+str(len(eModel.text)))
    # was from text
    #   db.from_documents(eModel.toDocument(), embedding=hf, elasticsearch_url=es_url, index_name=settings.ES_INDEX )

    db.from_documents(pages, embedding=hf, elasticsearch_url=es_url, index_name=settings.ES_INDEX_DOCUMENTS)
