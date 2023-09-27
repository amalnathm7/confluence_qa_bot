"""Module defining a function that extracts and returns the texts in a Confluence space"""
import os
from dotenv import load_dotenv
from langchain.document_loaders import ConfluenceLoader
from langchain.text_splitter import TokenTextSplitter

load_dotenv()

confluence_username = os.environ.get("CONFLUENCE_USERNAME")
confluence_api_key = os.environ.get("CONFLUENCE_API_KEY")
confluence_url = os.environ.get("CONFLUENCE_URL")
confluence_space_key = os.environ.get("CONFLUENCE_SPACE_KEY")


def extract_documents():
    """Function to extract documents from Confluence space"""
    loader = ConfluenceLoader(
        url=confluence_url,
        username=confluence_username,
        api_key=confluence_api_key
    )

    documents = loader.load(
        space_key=confluence_space_key,
        limit=100,
        max_pages=100
    )

    text_splitter = TokenTextSplitter(
        chunk_size=1000, chunk_overlap=10, encoding_name="cl100k_base")
    texts = text_splitter.split_documents(documents)

    return texts
