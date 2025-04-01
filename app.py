import streamlit as st
from assistant.chat_engine import get_chat_chain
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(page_title="AI Study Assistant", layout="centered")
st.title("📚 AI Study Assistant")

subject = st.selectbox("Select Subject", ["English", "Math", "Science", "Social Studies"])

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
    st.session_state.chain = get_chat_chain(subject)

# Reset memory if subject changes
if subject != st.session_state.get("current_subject"):
    st.session_state.chain = get_chat_chain(subject)
    st.session_state.chat_history = []
    st.session_state.current_subject = subject

user_input = st.text_input("Ask your question:", key="input")

if st.button("Send") and user_input:
    response = st.session_state.chain.run(input=user_input)
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("AI", response))

for speaker, message in st.session_state.chat_history:
    with st.chat_message(speaker.lower()):
        st.markdown(message)