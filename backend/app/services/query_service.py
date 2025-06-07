from openai import OpenAI
from app.config import OPENAI_API_KEY
from chromadb import Client
from chromadb.config import Settings

client_ai = OpenAI(api_key=OPENAI_API_KEY)

client = Client(Settings(anonymized_telemetry=False))
collection = client.get_or_create_collection(name="documind")

def embed_query(query: str) -> list:
    response = client_ai.embeddings.create(
        input=[query],
        model="text-embedding-ada-002"
    )
    return response.data[0].embedding

def query_documents(question: str, top_k: int = 5):
    query_embedding = embed_query(question)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    combined = []
    for doc, meta in zip(results['documents'][0], results['metadatas'][0]):
        combined.append({
            "doc_id": meta["doc_id"],
            "chunk_index": meta["chunk"],
            "text": doc
        })

    return combined
