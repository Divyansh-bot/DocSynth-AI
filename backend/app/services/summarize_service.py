from openai import OpenAI
from app.config import OPENAI_API_KEY

client_ai = OpenAI(api_key=OPENAI_API_KEY)

def generate_theme_summary(question: str, document_chunks: list) -> str:
    context = "\n\n".join(
        f"Doc: {chunk['doc_id']} - Chunk {chunk['chunk_index']}:\n{chunk['text']}"
        for chunk in document_chunks
    )

    prompt = f"""
You are an AI assistant helping with research. A user has asked the following question:

"{question}"

Below are chunks of text from various documents. Please:
1. Identify common themes.
2. Provide a clear, grouped summary with citations like (Doc: DOC001, Chunk 2).

Context:
{context}
"""

    response = client_ai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4
    )

    return response.choices[0].message.content
