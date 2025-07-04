from dataIngestion import PDF_Loader

from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS

def create_embeddings():
    doc=PDF_Loader('Data/News Popularity Analysis.pdf')
    embeddings= (
        OllamaEmbeddings(model="gemma2:2b")
    )
    vectorStore=FAISS.from_documents(doc,embeddings)
    vectorStore.save_local("VectorDB/index")

create_embeddings()
