'''
Not really a true implementation of the factory pattern , even if the intent is the same

Manufacture the (Lang)Chains we need in our app
'''

import os

import settings.config as config
import settings.token_loader as token_loader
import templates.prompts as prompts
from service import rag_factory as rag_factory
from langchain.output_parsers.openai_functions import JsonOutputFunctionsParser
from langchain.prompts.chat import ChatPromptTemplate
from langchain.schema.runnable import Runnable
#from langchain_community.chat_models.openai import ChatOpenAI
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI

prompt_func = {
    "name": "email_draft",
    "description": "Draft a response to a client or colleague email",
    "parameters": {
        "type": "object",
        "properties": {
            "inemail": {"type": "string", "description": "The text of the incoming email"},
            "outemail": {
                "type": "string",
                "description": "The suggested text to use in the email response",
            },
        },
        "required": ["inemail", "outemail"],
    },
}


# def get_sample_chain() -> Runnable:
#     '''
#     Only keeping as reference - can be removed
#     '''
#     # Get the open AI key and set as env variable
#     token = token_loader.setup_token("openai")
#     os.environ["OPENAI_API_KEY"] = token


#     """Return a chain."""
#     prompt = ChatPromptTemplate.from_template("respond to an email about {topic}")    
#     model = ChatOpenAI().bind(functions=[prompt_func], function_call={"name": "email_draft"})
#     parser = JsonOutputFunctionsParser()
#     return prompt | model | parser







def get_chain() -> Runnable:

    # Get the open AI key and set as env variable
    #TODO refactor
    token = token_loader.setup_token("openai")
    os.environ["OPENAI_API_KEY"] = token


    ELASTIC_INDEX_NAME= config.read("ES_INDEX_KB")


    """Return a chain."""
    prompt = ChatPromptTemplate.from_template(prompts.TEMPLATE_EMAIL_PROMPT_2)
    retriever = rag_factory._get_setup_knowledgebase_retriever(ELASTIC_INDEX_NAME)
    model = ChatOpenAI().bind(functions=[prompt_func], function_call={"name": "email_draft"})
    parser = JsonOutputFunctionsParser()

    # include all known
    # DEAD ENDrag_chain =  prompt | {"context": retriever, "question": RunnablePassthrough()} | model | parser

    # next try - https://github.com/elastic/elasticsearch-labs/blob/main/notebooks/langchain/self-query-retriever-examples/chatbot-with-bm25-only-example.ipynb

    # previous simple prompt | retriever| model | parser
    rag_chain = prompt | model | parser



    return rag_chain