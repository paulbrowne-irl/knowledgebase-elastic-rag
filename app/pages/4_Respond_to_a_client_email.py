import streamlit as st

import util.rag.lc_controller as lc_controller
import app as app
import pages.app_sidebaridebar as app_sidebar
import templates.prompts

from importlib import reload


#Window setup
st.title('Draft a client email')

#Fields on Sidebar
reload(app_sidebar)

#make sure setup gets run at start
lc_controller.setup()


# reload previous prompot
if 'prompt' not in st.session_state:
    st.session_state['prompt'] = templates.prompts.TEMPLATE_EMAIL_PROMPT


#############
# Main UI

with st.form('my_form'):
    input_text = st.text_area('Enter text:', 'Dear Sir / Madam, please tell me about the supports you offer engineering companies, sincerely, Ms J Client')
    submitted = st.form_submit_button('Submit')
    

    # check we have a link
    #if not document_search.startswith('All'):
    #    st.warning('Elastic filtering not implented yet!', icon='⚠')

    # Tabs setup
    tab_answer, tab_context, tab_prompt = st.tabs(["Draft Email", "Context", "Prompt Template"])

    #check we need to generate check
    if submitted:

        # Find nearest match documents
        similar_docs = lc_controller.get_nearest_match_documents(app_sidebar.document_search, input_text)
   
        ## Ask Local LLM context informed prompt
        informed_context= similar_docs[0].page_content
        llm_chain = lc_controller.get_llm_chain(st.session_state['prompt'])
        informed_response = llm_chain.run(context=informed_context,question=input_text)

        #update the UI with the answer
        with tab_answer:
           st.header('Answer')
           st.info(informed_response)
            
        with tab_context:
            st.header('Relevant Documents for this answer')
            st.info(similar_docs)
            
        with tab_prompt:
            st.header('Prompt to the LLM')
            st.info(st.session_state['prompt'])
                