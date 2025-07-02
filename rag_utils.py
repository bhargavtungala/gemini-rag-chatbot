import os
import chromadb
from langchain_google_vertexai import VertexAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

# ChromaDB setup
client = chromadb.PersistentClient(path="chroma_store")
collection = client.get_or_create_collection(name="docs")


# Embeddings
embedding_function = VertexAIEmbeddings(model_name="text-embedding-004")


def ingest_text(text, doc_id):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    chunks = splitter.split_text(text)

    vectors = embedding_function.embed_documents(chunks)
    ids = [f"{doc_id}_{i}" for i in range(len(chunks))]
    collection.add(documents=chunks, embeddings= vectors, ids=ids)
    
    existing = collection.get(ids=[doc_id], include=[])
    if existing and existing["ids"]:
        return

def retrieve_similar(query, k=3):
    query_vector = embedding_function.embed_query(query)
    results = collection.query(
        query_embeddings=[query_vector],
        n_results=k
    )
    return results['documents'][0]
