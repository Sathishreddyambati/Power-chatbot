import streamlit as st
from chatbot import get_bot_response

st.set_page_config(page_title="Power Chatbot", page_icon="⚡")
st.title("⚡ Power - Your Free AI Chatbot")

st.markdown("Ask me anything! I'm your free AI assistant.")

user_input = st.text_input("You:", key="input")

if user_input:
    with st.spinner("Power is thinking..."):
        response = get_bot_response(user_input)
        st.success(response)