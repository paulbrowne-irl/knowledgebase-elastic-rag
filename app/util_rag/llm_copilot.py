from __future__ import annotations

import asyncio
import os

from langchain_core.callbacks.manager import CallbackManagerForLLMRun
from langchain_core.language_models.llms import LLM

from typing import Any
from typing import Mapping
from typing import List
from typing import Optional

import logging

from sydney import SydneyClient



# Notes
# Sydney copilot setup
# https://github.com/vsakkas/sydney.py

# Custom LLM
# https://python.langchain.com/docs/modules/model_io/llms/custom_llm

# note use of annotations


class CustomLLM(LLM):
    '''
    Customer Langchain LLM to invote copilot
    '''
    copilot_token: str

    @property
    def _llm_type(self) -> str:
        return "custom call to Copilot"
    

    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> str:
        '''
        Call to invoke llm goes here
        '''
        
        if stop is not None:
            raise ValueError("stop kwargs are not permitted.")

        os.environ["BING_COOKIES"]=self.copilot_token
        #print ("set token to :"+self.copilot_token)
        

        # actual code to invoke copilot using Sydney
        print ("Calling copilot using prompt:"+prompt)
        response = asyncio.run (self.call_copilot(prompt))

        return response

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        """Get the identifying parameters."""
        return {"copilot_token": self.copilot_token}


    # Standard sydney call
    async def call_copilot(self,prompt) -> str:
        async with SydneyClient() as sydney:
            
            logging.debug("Awaiting response from Sydney.", end="", flush=True)

            resp = await(sydney.ask(prompt))

            logging.debug("response recieved")
            
            return resp
        

