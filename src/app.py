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

get_answer_button = st.button('Get Answer', key="get_answer_button")

if get_answer_button:
    with st.spinner("Running..."):
        answer = confluence_qa_bot.run(question)

    st.success('Done!')
    st.write(answer)
else:
    st.text("Click 'Get Answer' to retrieve the answer")
