import streamlit as st
import util.rag.rag_controller as rag_controller
import logging

#Set the Logging level. Change it to logging.INFO is you want just the important info
#logging.basicConfig(filename=config.read("LOG_FILE"), encoding='utf-8', level=logging.DEBUG)
logging.basicConfig(level=logging.DEBUG)

st.set_page_config(
    page_title="Proof of concept",
    page_icon=":bar_chart:",
)


st.header("DA support tools")
st.caption("for Product and Portfolio Management")

st.markdown(
    """
    Pick an App on the left hand side to learn more
    """
)


