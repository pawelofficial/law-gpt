import streamlit as st
from src import utils

# Define your username and password
USERNAME = "admin"
PASSWORD = "admin"

def authenticate(username, password):
    return username == USERNAME and password == PASSWORD

# Authentication form
def login():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if authenticate(username, password):
            st.session_state["authenticated"] = True
            st.rerun()
        else:
            st.error("Invalid username or password")

# Check if the user is authenticated
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    login()
else:
    st.title("Merger Agreement chatbot")

    # Initialize chat history
    def reinit_session_state():
        pass  # Your existing code here
    

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
if st.session_state["authenticated"]:
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