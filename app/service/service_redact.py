import logging
from pprint import pprint
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

#handle to the most recent redaction
redacted_mappings = {}

@app.post("/redact_doc")
def redact_doc(docToRedact:Document)->Document:
    '''
    "overloaded" method - takes and returns langchain doc
    '''
    redacted_text = redact_text(docToRedact.page_content)
    docToRedact.page_content=redacted_text

    return docToRedact


@app.post("/redact_text")
def redact_text(textToRedact:str)->str:
    '''
    Redact text using Spacy rules - removing people, company names, telephone numbers
    '''

    global redacted_mappings

    replaced_text, regex_mapping = cleaner.replace_regex(textToRedact)
    replaced_text, entity_mapping = cleaner.replace_ner(replaced_text)
    new_redacted_mappings = {**regex_mapping, **entity_mapping}
    colored_anonymized_text = cleaner.add_color(replaced_text, new_redacted_mappings)

    #add to our previous redactions
    redacted_mappings = redacted_mappings | new_redacted_mappings
    
    return colored_anonymized_text

@app.post("/deanonymize_doc")
def deanonymize_doc(redacted_doc:Document)->Document:
    
    '''
    "overloaded" method - takes and returns langchain doc
    '''
    clear_text = deanonymize_text(redacted_doc.page_content)
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
        page_content='''Peter Parker works as the CEO of a company called ACME engineering. He lives in Dublin and his phone number is 01-234567
        Diana Prince is the co-founder of a company called BionMedical . She lives in Galway and her phone number is 01-234567
        ''',
        metadata={"source": "local_est"}
    )
    print("Original:"+str(text_document))


    #test redact
    redacted_doc = redact_doc(text_document)

    print(f"{Colors.BOLD}{Colors.OKCYAN}\nUse the following anonymized text:\n{Colors.ENDC}{redacted_doc}")

    removed_info_summary = ', '.join(list(redacted_mappings.keys()))
    print(f"{Colors.BOLD}{Colors.PURPLE}\nRemoved sensitive information: {removed_info_summary}{Colors.ENDC}")

    #test restore
    deanonymized_doc = deanonymize_doc(redacted_doc)

    print(f"{Colors.BOLD}{Colors.OKCYAN}\nPrivate information restored:{Colors.ENDC}\n{deanonymized_doc}\n")

    #repeat redact to check we get increment
    # text_document2 = Document(
    #     page_content="Diana Prince is the co-founder of a company called BionMedical . She lives in Galway and her phone number is 01-234567",
    #     metadata={"source": "local_est"}
    # )

    # redacted_doc = redact_doc(text_document2)


    print("\n\n\n")
    pprint(redacted_mappings)