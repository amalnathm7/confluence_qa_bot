"""Module that defines functions to create a chroma DB, store and retrieve vectors"""
import os
import shutil
from dotenv import load_dotenv
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from confluence_extractor import extract_documents

load_dotenv()

PERSIST_DIRECTORY = "./chroma_db/"
embedding = OpenAIEmbeddings()


def load_db():
    """Load or create the Chroma vector store with documents and embeddings."""
    if os.path.exists(PERSIST_DIRECTORY):
        shutil.rmtree(PERSIST_DIRECTORY)
    return Chroma.from_documents(
        documents=extract_documents(), embedding=embedding, persist_directory=PERSIST_DIRECTORY)


vectordb = load_db()


def get_retriever(k: int):
    """Return a retriever object of the existing Chroma vector store."""

    return vectordb.as_retriever(search_kwargs={"k": k})
