'''
Not really a true implementation of the factory pattern , even if the intent is the same

Manufacture the (Lang)Chains we need in our app
'''

from langchain_openai import ChatOpenAI
#from langchain_community.chat_models.openai import ChatOpenAI
from langchain.output_parsers.openai_functions import JsonOutputFunctionsParser
from langchain.prompts.chat import ChatPromptTemplate
from langchain.schema.runnable import Runnable
import os
import settings.config as config
import settings.token_loader as token_loader

prompt_func = {
    "name": "email_draft",
    "description": "Draft a aesponse to a client or colleague email",
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


def get_sample_chain() -> Runnable:
    '''
    Only keeping as reference - can be removed
    '''
    # Get the open AI key and set as env variable
    token = token_loader.setup_token("openai")
    os.environ["OPENAI_API_KEY"] = token


    """Return a chain."""
    prompt = ChatPromptTemplate.from_template("respond to an email about {topic}")    
    model = ChatOpenAI().bind(functions=[prompt_func], function_call={"name": "email_draft"})
    parser = JsonOutputFunctionsParser()
    return prompt | model | parser







def get_chain() -> Runnable:

    # Get the open AI key and set as env variable
    token = token_loader.setup_token("openai")
    os.environ["OPENAI_API_KEY"] = token


    """Return a chain."""
    prompt = ChatPromptTemplate.from_template("tell me a joke about {topic}")
    model = ChatOpenAI().bind(functions=[prompt_func], function_call={"name": "email_draft"})
    parser = JsonOutputFunctionsParser()
    return prompt | model | parser