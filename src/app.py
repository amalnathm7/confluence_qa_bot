"""Main module"""
import streamlit as st
from openai_bot import bot


def run_streamlit_ui():
    """Function to run the website"""
    st.set_page_config(
        page_title='Q&A Bot for Confluence',
        page_icon='⚡',
    )

    confluence_qa_bot = bot()

    st.title("KeyValue Confluence Q&A")

    question = st.text_input('Ask a question', "Tell me about KeyValue.")

    button_running = False

    get_answer_button = st.button('Get Answer')

    if get_answer_button:
        with st.spinner("Running..."):
            answer = confluence_qa_bot.run(question)

        button_running = False

        st.success(answer)
    else:
        if not button_running:
            st.text("Click 'Get Answer' to retrieve the answer")
        else:
            st.button('Get Answer', key="get_answer_button", disabled=True)


if __name__ == "__main__":
    run_streamlit_ui()
