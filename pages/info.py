import streamlit as st 


s="""
This is a gpt fine tuned LLM for talking to this document https://contracts.justia.com/companies/amgen-inc-93/contract/565667/

currently it can only zero shot a question answer, aka you can ask 
    What is this agreement about?
You get an answer, but there is no follow up available, aka this wont work:
    - What is this agreement about?
    - This is an agreement is about XXX
    - Are you sure? ( this will be sent as a standalone question rather than a follow up to above conversation)
"""

st.write(s)