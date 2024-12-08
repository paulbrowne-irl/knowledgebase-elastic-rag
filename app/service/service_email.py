import logging

import service.service_redact as service_redact
import settings.config as config
import uvicorn
from fastapi import FastAPI
from service import rag_factory as rag_factory
from templates import prompts as prompts

#setup logging
logger = logging.getLogger("")
logger.setLevel(logging.DEBUG)

# setup once
app = FastAPI(title="Email Response Service")


'''
This module provides a server facade to auto draft emails
a) it can be run as a uvicorn fastapi server 
     uvicorn service.service_email:app 

b) it can be called directly by the app and front end bots

Auto generated api docs (on running server) - localhost:8000/docs

'''

@app.get("/service_check")
@app.post("/service_check")
def service_check():
    return "ok"

# @app.post("/test_email")
# def test_email(email: str):
#     return "world "+email

@app.get("/draft_email_response")
@app.post("/draft_email_response")
def draft_email_response(email: str):

    #read config infor
    REDACT_INFO = config.read_boolean("REDACT_PRIVATE_INFO")
    ELASTIC_INDEX_NAME= config.read("ES_INDEX_KB")


    # Redact information before we go further
    if(REDACT_INFO):
        email = service_redact.redact_text(email)

    # Find nearest match documents
    similar_docs = rag_factory.get_nearest_match_documents(ELASTIC_INDEX_NAME,email)
    logging.info("relevant docs:"+str(similar_docs))

    #redact these if needed
    if(REDACT_INFO):
        new_doc_list =[]
        for doc in similar_docs:
            new_doc_list.append(service_redact.redact_doc(doc))
        similar_docs = new_doc_list


    #generate the chain using the prompt
    llm_chain = rag_factory.get_llm_chain(prompts.TEMPLATE_EMAIL_PROMPT)

    
    # Adjust your code to include an 'input' dictionary
    input_data = {
        'context': similar_docs,
        'question': email
    }


    # Now, pass the 'input_data' dictionary to the 'invoke' method
    informed_response = llm_chain.invoke(input=input_data)

    #restore text if needed
    if(REDACT_INFO):
        informed_response = service_redact.deanonymize_text(str(informed_response))

    return {"suggested_text": informed_response}



# start server when called via command line
if __name__ == "__main__":
    uvicorn.run("service_email:app", host="0.0.0.0", port=8000)    