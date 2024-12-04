import streamlit as st
import logging

#Set the Logging level. Change it to logging.INFO is you want just the important info
logging.basicConfig(level=logging.INFO)

st.set_page_config(
    page_title="Proof of concept",
    page_icon=":email:",
)


st.header("AI Support tools")
st.caption("for Enterprise Email and Knowledge Management")

st.markdown(
    """
    Pick an App on the left hand side to learn more
    """
)


