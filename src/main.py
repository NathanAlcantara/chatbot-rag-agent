import os
from fastapi import FastAPI
from src.rag_pipeline import embed_and_store, search

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Chatbot is up and running!"}

@app.post("/embed/")
def embed_documents(documents: list[str]):
    embed_and_store(documents)
    return {"message": f"Successfully embedded {len(documents)} documents"}

@app.get("/search/")
def search_documents(query: str):
    results = search(query)
    return {"results": results}