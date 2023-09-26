"""Module defining a function that extracts and returns the texts in a Confluence space"""
import os
from dotenv import load_dotenv
from langchain.document_loaders import ConfluenceLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.text_splitter import TokenTextSplitter

load_dotenv()

confluence_username = os.getenv("CONFLUENCE_USERNAME")
confluence_api_key = os.getenv("CONFLUENCE_API_KEY")
confluence_url = os.getenv("CONFLUENCE_URL")
confluence_space_key = os.getenv("CONFLUENCE_SPACE_KEY")


def extract_documents():
    """Function to extract documents from Confluence space"""
    loader = ConfluenceLoader(
        url=confluence_url,
        username=confluence_username,
        api_key=confluence_api_key
    )

    documents = loader.load(
        space_key=confluence_space_key,
        limit=100
    )

    text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0)
    texts = text_splitter.split_documents(documents)
    text_splitter = TokenTextSplitter(
        chunk_size=1000, chunk_overlap=10, encoding_name="cl100k_base")
    texts = text_splitter.split_documents(texts)

    return texts
