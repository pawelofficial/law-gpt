import streamlit as st
from src import utils

st.title("Echo Bot")



# Initialize chat history
def reinit_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = []

def display_history(N=50):
# Display chat messages from history on app rerun
    for message in st.session_state.messages[:N]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])





reinit_session_state()
display_history()

# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = utils.send_request('chat_response', {"user_prompt": prompt},method='POST')['response']
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})