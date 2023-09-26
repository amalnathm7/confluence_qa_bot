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

BUTTON_RUNNING = False

get_answer_button = st.button('Get Answer')

if get_answer_button:
    with st.spinner("Running..."):
        answer = confluence_qa_bot.run(question)

    BUTTON_RUNNING = False

    st.success('Done!')
    st.write(answer)
else:
    if not BUTTON_RUNNING:
        st.text("Click 'Get Answer' to retrieve the answer")
    else:
        st.button('Get Answer', key="get_answer_button", disabled=True)
