"""Module that defines functions to create a chroma DB, store and retrieve vectors"""
from dotenv import load_dotenv
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from confluence_extractor import extract_documents

load_dotenv()

PERSIST_DIRECTORY = "./chroma_db/"


def get_retriever(k: int):
    """Function that returns a retriever object of the vectorstore"""
    embedding = OpenAIEmbeddings()

    vectordb = Chroma.from_documents(
        documents=extract_documents(), embedding=embedding, persist_directory=PERSIST_DIRECTORY)

    return vectordb.as_retriever(search_kwargs={"k": k})
