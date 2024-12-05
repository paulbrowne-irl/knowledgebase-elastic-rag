import streamlit as st

from service import rag_factory as rag_factory
import templates.prompts
import pages.support.app_sidebar as app_sidebar
from importlib import reload

if 'prompt' not in st.session_state:
    st.session_state['prompt'] = templates.prompts.TEMPLATE_QA_PROMPT


#Window setup
st.title('Hello DA! How can I help you?')

#Fields on Sidebar
reload(app_sidebar)

#############
# Main UI

with st.form('my_form'):
    input_text = st.text_area('Enter text:', 'Can a company apply for ... ?')
    submitted = st.form_submit_button('Submit')
    

    # check we have a link
    #if not document_search.startswith('All'):
    #    st.warning('Elastic filtering not implented yet!', icon='⚠')


    # Tabs setup
    tab_answer, tab_context, tab_prompt = st.tabs(["Answer", "Context", "Prompt Template"])

    #check we need to generate check
    if submitted:
        
        with st.status ("Checking to see if I understand your question ...") as status:

            similar_docs = rag_factory.get_nearest_match_documents(app_sidebar.document_search, input_text)
    
            # Update prompt
            status.update(label="Searching through the information I have been told about..",state="running", expanded=False)
            informed_context= similar_docs[0].page_content

            #get the llm chain to handle this
            llm_chain = rag_factory.get_llm_chain(st.session_state['prompt'])

            status.update(label="Getting you an answer",state="running", expanded=False)
            #informed_response = llm_chain.invoke(input={},context=informed_context,question=input_text)

            input={"context":informed_context,
                   "question": input_text
                   }

            informed_response = llm_chain.invoke(input=input)

            status.update(label="Here is your answer", state="complete", expanded=False)


            #update the UI with the answer
            with tab_answer:
                st.header('Answer')
                st.info(informed_response['text'])
                
            with tab_context:
                    st.header('Relevant Documents for this answer')
                    st.info(similar_docs)
                
            with tab_prompt:
                    st.header('Prompt to the LLM')
                    st.info(st.session_state['prompt'])
                