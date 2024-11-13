import logging
import settings.config as config
import uvicorn
from fastapi import FastAPI#
from service import rag_factory as rag_factory
from templates import prompts as prompts

from langchain_core.documents import Document

from util.redact.cleanprompt import PromptCleaner
from util.redact.cleanprompt import Colors

app = FastAPI(title="Prompt Redaction Service")

#handle to our PromptCleaner
cleaner = PromptCleaner()

#handle to the most recent redactino
redacted_mappings = {}

@app.post("/redact_doc")
def redact_doc(docToRedact:Document)->Document:
    '''
    "overloaded" method - takes and returns langchain doc
    '''
    text_to_redact = str(docToRedact)
    redacted_text = redact_text(text_to_redact)
    docToRedact.page_content=redacted_text

    return docToRedact


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

@app.post("/deanonymize_doc")
def deanonymize_doc(redacted_doc:Document)->Document:
    
    '''
    "overloaded" method - takes and returns langchain doc
    '''
    text_to_deanon = str(redacted_doc)
    clear_text = redact_text(text_to_deanon)
    redacted_doc.page_content=clear_text

    return redacted_doc


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


    #create document
    text_document = Document(
        page_content="Peter Parker works as the CEO of a company called ACME engineering. He lives in Dublin and his phone number is 01-234567",
        metadata={"source": "local_est"}
    )

    #test redact
    redacted_doc = redact_doc(text_document)

    print(f"{Colors.BOLD}{Colors.OKCYAN}\nUse the following anonymized text:\n{Colors.ENDC}{redacted_doc}")

    removed_info_summary = ', '.join(list(redacted_mappings.keys()))
    print(f"{Colors.BOLD}{Colors.PURPLE}\nRemoved sensitive information: {removed_info_summary}{Colors.ENDC}")

    #test restore
    deanonymized_doc = deanonymize_doc(redacted_doc)

    print(f"{Colors.BOLD}{Colors.OKCYAN}\nPrivate information restored:{Colors.ENDC}\n{deanonymized_doc}\n")