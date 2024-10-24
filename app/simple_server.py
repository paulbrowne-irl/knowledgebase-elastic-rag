import logging
import settings.config as config
import uvicorn
from fastapi import FastAPI#
from service import rag_factory as rag_factory
from templates import prompts as prompts

# setup once
app = FastAPI(title="LangServe Knowledgebase Example")
ELASTIC_INDEX_NAME= config.read("ES_INDEX_KB")

'''
This module provides a service
a) it can be run as a uvicorn fastapi server
b) it can be called directly by the app and front end bots
'''


@app.post("/draft_email")
def draft_email(input_email: str):


    # Find nearest match documents
    similar_docs = rag_factory.get_nearest_match_documents(ELASTIC_INDEX_NAME,input_email)
    logging.info("relevant docs:"+str(similar_docs))

    #generate the chain using the prompt
    llm_chain = rag_factory.get_llm_chain(prompts.TEMPLATE_EMAIL_PROMPT)

    
    # Adjust your code to include an 'input' dictionary
    input_data = {
        'context': similar_docs,
        'question': input_email
    }


    # Now, pass the 'input_data' dictionary to the 'invoke' method
    informed_response = llm_chain.invoke(input=input_data)

    return {"suggested_text": informed_response}




'''
Previous Langserve code - possible to restore in future iteration
'''
# def start():

#     '''
#     Lang Serve server which makes Lang chain available via REST API
#     When run normally, it is available via http://localhost:8001/docs
#     '''

#     app = FastAPI(title="LangServe Knowledgebase Example")
#     add_routes(app, get_chain())

#     logging.info("Starting LangServe on http://localhost:8001")
#     


# when called via command line
if __name__ == "__main__":
    uvicorn.run("simple_server:app", host="0.0.0.0", port=8001)    