from langserve import add_routes
from lang_server.chain_factory import get_chain
from lang_server import lc_controller as lc_controller


import uvicorn
import logging

from fastapi import FastAPI

from templates import prompts as prompts

#refactor
import settings.config as config


app = FastAPI(title="LangServe Knowledgebase Example")
ELASTIC_INDEX_NAME= config.read("ES_INDEX_KB")


@app.post("/draft_email")
def read_root(input_email: str):


    # Find nearest match documents
    similar_docs = lc_controller.get_nearest_match_documents(ELASTIC_INDEX_NAME,input_email)
    logging.info("relevant docs:"+str(similar_docs))

    ## Ask Local LLM context informed prompt
    informed_context= similar_docs[0].page_content

    #generate the chain using the prompt
    llm_chain = lc_controller.get_llm_chain_old(prompts.TEMPLATE_EMAIL_PROMPT)

    #informed_response = llm_chain.run(context=informed_context,question=this_question)
    informed_response = llm_chain.invoke("context": lambda x: informed_context, "question": input_email)
    

    return informed_response, similar_docs
    return {"suggested_text": informed_response,
            "similar_docs":informed_context}



# def start():

#     '''
#     Lang Serve server which makes Lang chain available via REST API
#     When run normally, it is available via http://localhost:8001/docs
#     '''

#     app = FastAPI(title="LangServe Knowledgebase Example")
#     add_routes(app, get_chain())

#     logging.info("Starting LangServe on http://localhost:8001")
#     uvicorn.run(app, host="0.0.0.0", port=8001)


# # when called via command line
# if __name__ == "__main__":
#     start()    