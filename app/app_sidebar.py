import streamlit as st

'''
The python code in this file is run on import - so importing in each page
will give us a common sidebar.
'''

#Fields on Sidebar

try:
    document_search = st.sidebar.selectbox( 'Source Information', ('Knowledgebase','Other Source'))

    # POC reminder
    st.sidebar.info("Proof of concept")

except st.errors.DuplicateWidgetID:
    print ("Ignoring intial duplicate error")
