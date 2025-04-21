import os
from fastapi import FastAPI
from src.rag_pipeline import embed_and_store, search

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Chatbot is up and running!"}


@app.get("/embed/")
def embed_documents():
    documents = embed_and_store()
    return {"message": f"Successfully embedded {len(documents['ids'])} documents"}


@app.get("/search/")
def search_documents(query):
    results = search(query)
    return {"results": results}
