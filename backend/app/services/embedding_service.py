import os
from openai import OpenAI
from app.config import OPENAI_API_KEY
from chromadb import Client
from chromadb.config import Settings

# OpenAI client
client_ai = OpenAI(api_key=OPENAI_API_KEY)

# ChromaDB client
client = Client(Settings(anonymized_telemetry=False))
collection = client.get_or_create_collection(name="documind")

def embed_text(text: str) -> list:
    response = client_ai.embeddings.create(
        input=[text],
        model="text-embedding-ada-002"
    )
    return response.data[0].embedding

def store_document_embedding(doc_id: str, text_chunks: list):
    for i, chunk in enumerate(text_chunks):
        emb = embed_text(chunk)
        collection.add(
            documents=[chunk],
            embeddings=[emb],
            ids=[f"{doc_id}_{i}"],
            metadatas=[{"doc_id": doc_id, "chunk": i}]
        )
