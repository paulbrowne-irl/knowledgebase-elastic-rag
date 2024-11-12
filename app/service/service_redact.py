import logging
import settings.config as config
import uvicorn
from fastapi import FastAPI#
from service import rag_factory as rag_factory
from templates import prompts as prompts

from util.redact.cleanprompt import PromptCleaner
from util.redact.cleanprompt import Colors

app = FastAPI(title="Prompt Redaction Service")

#handle to our PromptCleaner
cleaner = PromptCleaner()

#handle to the most recent redactino
redacted_mappings = {}

@app.post("/redact_text")
def redact_text(textToRedact:str)->str:
    '''
    Redact text using Spacy rules - removing people, company names, telephone numbers
    '''

    global redacted_mappings

    #instruction_initial = "Welcome to CleanPrompt! Enter/paste your text. Type 'END' on a new line and press enter to submit:"
    #text = get_multiline_input(instruction_initial) # get text from user which potentially includes sensitive info
    replaced_text, regex_mapping = cleaner.replace_regex(textToRedact)
    replaced_text, entity_mapping = cleaner.replace_ner(replaced_text)
    redacted_mappings = {**regex_mapping, **entity_mapping}


    
    colored_anonymized_text = cleaner.add_color(replaced_text, redacted_mappings)
    
    
    return colored_anonymized_text


@app.post("/deanonymize_text")
def deanonymize_text(redacted_text:str)->str:
    '''
    restore previously hidden information
    '''

    global redacted_mappings
    
    #instruction_final = "Enter/paste the response from your LLM. Type 'END' on a new line and press enter to submit:"
    #LLM_text = get_multiline_input(instruction_final)
    deanonymized_text = cleaner.revert_text(redacted_text, redacted_mappings, color=True)

    return deanonymized_text
    



if __name__ == "__main__":

    #text
    text="Peter Parker works as the CEO of a company called ACME engineering. He lives in Dublin and his phone number is 01-234567"
    print("\n\nOriginal:"+text)


    #test redact
    redacted_text = redact_text(text)

    print(f"{Colors.BOLD}{Colors.OKCYAN}\nUse the following anonymized text:\n{Colors.ENDC}{redacted_text}")

    removed_info_summary = ', '.join(list(redacted_mappings.keys()))
    print(f"{Colors.BOLD}{Colors.PURPLE}\nRemoved sensitive information: {removed_info_summary}{Colors.ENDC}")

    #test restore
    deanonymized_text = deanonymize_text(redacted_text)

    print(f"{Colors.BOLD}{Colors.OKCYAN}\nPrivate information restored:{Colors.ENDC}\n{deanonymized_text}\n")