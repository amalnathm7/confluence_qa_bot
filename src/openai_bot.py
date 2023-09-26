"""Module defining a function that returns an OpenAI bot that answers queries
    based on the documents stored in the Chroma vectorstore"""
import os
from dotenv import load_dotenv
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from chroma_db import get_retriever

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
LLM_OPENAI_GPT35 = 'gpt-3.5-turbo'
CUSTOM_PROMPT_TEMPLATE = """You are a Confluence chatbot answering questions.
Use the following pieces of context to answer the question at the end.
If you don't know the answer, say that you don't know, don't try to make up an answer.
{context}
Question: {question}
Helpful Answer:"""


def bot():
    """Function that returns an openAI bot that can answer document related queries"""
    custom_prompt = PromptTemplate(
        template=CUSTOM_PROMPT_TEMPLATE, input_variables=[
            "context", "question"]
    )

    llm = ChatOpenAI(model_name=LLM_OPENAI_GPT35, temperature=0.)

    retriever = get_retriever(k=4)

    chain_type_kwargs = {"prompt": custom_prompt}

    retrieval_chain = RetrievalQA.from_chain_type(
        llm=llm, chain_type="stuff", retriever=retriever, chain_type_kwargs=chain_type_kwargs)

    return retrieval_chain
