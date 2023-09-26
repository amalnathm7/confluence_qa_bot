"""Module that defines functions to create a chroma DB, store and retrieve vectors"""
import os
from dotenv import load_dotenv
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from confluence_extractor import extract_documents

load_dotenv()

persist_directory = os.getenv("CHROMA_PERSIST_DIRECTORY")


def get_retriever(k: int):
    """Function that returns a retriever object of the vectorstore"""
    embedding = OpenAIEmbeddings()

    vectordb = Chroma.from_documents(
        documents=extract_documents(), embedding=embedding, persist_directory=persist_directory)
    
    return vectordb.as_retriever(search_kwargs={"k": k})
