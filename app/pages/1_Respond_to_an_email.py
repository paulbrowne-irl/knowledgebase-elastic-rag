import streamlit as st

#from service import rag_factory as rag_factory
import app as app
import pages.support.app_sidebar as app_sidebar
import templates.prompts

import pages.support.page_support_outlook as page_support_outlook

from importlib import reload


#Window setup
st.title('Auto Draft a client email :email:')

#Fields on Sidebar
reload(app_sidebar)


# reload previous prompt
if 'prompt' not in st.session_state:
    st.session_state['prompt'] = templates.prompts.TEMPLATE_EMAIL_PROMPT


#############
# Main UI

with st.form('my_form'):
    #input_text = st.text_area('Enter text:', 'Dear Sir / Madam, please tell me about the supports you offer engineering companies, sincerely, Ms J Client')
    submitted = st.form_submit_button('Submit')
    

    # check we have a link
    #if not document_search.startswith('All'):
    #    st.warning('Elastic filtering not implented yet!', icon='⚠')

    # Tabs setup
    tab_answer, tab_context, tab_prompt = st.tabs(["Draft Email", "Context", "Prompt Template"])

    #check we need to generate check
    if submitted:
        page_support_outlook.pseudomain()

       	#setup loop on page
			
            # Read Config and present on page
				
                #starting folder (email box / sub folder)
					
                    #reply as?
					
                    #start and end portion of text to send to LLM
					
                    #Go button
				
                # start in config (folders) - for each email
					
                    #get text from email
					# do call to llm using text
					# mark as "done" using category
					# reply 
					# do call using text
					# add text to email
				# Streamlit logging on screen (to show activity)
