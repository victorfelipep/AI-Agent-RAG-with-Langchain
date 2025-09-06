from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

base_folder = "base"

#Create database by loading pdf docs, dividing by chunks and vectoring them
def create_db():
    docs = load_docs()
    chunks = divide_chunks(docs)
    vector_chunks(chunks)

#Load pdf docs from "base" folder
def load_docs():
    loader = PyPDFDirectoryLoader(base_folder, glob="*.pdf")
    docs = loader.load()
    return docs

#Divide the doc in chunks with 2000 characters and overlapping 500.
def divide_chunks(docs):
    doc_separator = RecursiveCharacterTextSplitter(
        chunk_size=2000,
        chunk_overlap=500,
        length_function=len,
        add_start_index=True
    )
    chunks = doc_separator.split_documents(docs)
    return chunks

#Vectorize your chunks
def vector_chunks(chunks):
    db = Chroma.from_documents(chunks, OpenAIEmbeddings(), persist_directory="db")
    

create_db()