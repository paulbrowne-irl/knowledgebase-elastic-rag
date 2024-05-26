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



class TestLLM(LLM):
    '''
    Customer Langchain LLM to invote copilot
    '''
    copilot_token: str

    @property
    def _llm_type(self) -> str:
        return "custom call to Test - will always return same value"
    

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

        return "Test LLM Response always the same"

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        """Get the identifying parameters."""
        return {"test_values": "na"}

