"""Main module"""
import streamlit as st
from openai_bot import bot

st.set_page_config(
    page_title='Q&A Bot for Confluence',
    page_icon='⚡',
)

confluence_qa_bot = bot()

st.title("Confluence Q&A")

question = st.text_input('Ask a question', "Hi, who are you?")

if st.button('Get Answer'):
    answer = confluence_qa_bot.run(question)
    st.write(answer)
