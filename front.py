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
            st.experimental_rerun()
        else:
            st.error("Invalid username or password")

# Check if the user is authenticated
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    login()
else:
    st.title("Agreement chatbot")

    # Initialize chat history
    def reinit_session_state():
        pass  # Your existing code here