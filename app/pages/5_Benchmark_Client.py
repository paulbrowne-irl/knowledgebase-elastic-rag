import streamlit as st
import pages.app_sidebaridebar as app_sidebar


from importlib import reload

import util.rag.lc_controller as lc_controller


#Window setup
st.title('Benchmark my client against peers ...')

#Fields on Sidebar
reload(app_sidebar)

#make sure setup gets run at start
lc_controller.setup()


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