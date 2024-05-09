import streamlit as st

'''
The python code in this file is run on import - so importing in each page
will give us a common sidebar.
'''

#Fields on Sidebar

try:
    llm_to_use = st.sidebar.selectbox( 'Language Model and Approach', ('Copilot','Local LLM'))
    document_search = st.sidebar.selectbox( 'Source Information', ('Knowledgebase','Other Source'))

    # POC reminder
    st.sidebar.info("Proof of concept")

except st.errors.DuplicateWidgetID:
    print ("Ignoring intial duplicate error")
