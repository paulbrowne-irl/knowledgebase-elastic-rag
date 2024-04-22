import streamlit as st
import sidebar

from importlib import reload

import util.rag_controller as rag_controller




#Window setup
st.title('Let me know when ...')

#Fields on Sidebar
reload(sidebar)

#make sure setup gets run at start
rag_controller.setup()


#############
# Main UI

with st.form('my_form'):
    input_text = st.text_area('Enter text:', 'Feature coming soon ...')
    submitted = st.form_submit_button('Submit')
    

    # check we have a link
    #if not document_search.startswith('All'):
    #    st.warning('Elastic filtering not implented yet!', icon='⚠')

    # Tabs setup
    tab_answer, tab_context, tab_prompt = st.tabs(["Answer", "Context", "Prompt Template"])

    #check we need to generate check
    if submitted:
          pass