import streamlit as st

'''
The python code in this file is run on import - so importing in each page
will give us a common sidebar.
'''

#Fields on Sidebar

try:
    document_search = st.sidebar.selectbox( 'Source Information', ('knowledge_base','Other Source not yet set'))

    # POC reminder
    st.sidebar.info("Initial Deployment")

except st.errors.DuplicateWidgetID:
    print ("Sidebar - Ignoring initial duplicate error")