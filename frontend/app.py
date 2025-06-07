import streamlit as st
import requests
import os

BACKEND_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="DocuMind AI", layout="wide")
st.title("📚 DocuMind AI – Document Insight Chatbot")

st.markdown("Upload documents and ask natural language questions to extract themes and insights.")

# ---- Upload Section ----
st.header("📤 Upload Document")

uploaded_file = st.file_uploader("Choose a PDF or image file", type=["pdf", "png", "jpg", "jpeg"])

if uploaded_file:
    if st.button("Upload"):
        files = {"file": (uploaded_file.name, uploaded_file, uploaded_file.type)}
        res = requests.post(f"{BACKEND_URL}/api/upload", files=files)

        if res.status_code == 200:
            st.success("✅ File uploaded and processed successfully.")
        else:
            st.error("❌ Upload failed. Check backend or file format.")

# ---- Ask a Question ----
st.header("💬 Ask a Question")

query = st.text_input("Type your question related to uploaded documents...")

if st.button("Submit Query"):
    if not query:
        st.warning("Please enter a question first.")
    else:
        with st.spinner("Getting results..."):
            res = requests.post(f"{BACKEND_URL}/api/query", json={"question": query})

        if res.status_code == 200:
            data = res.json()
            st.subheader("📑 Relevant Document Excerpts")
            for match in data["document_matches"]:
                st.markdown(f"**{match['doc_id']} – Chunk {match['chunk_index']}**\n\n{match['text']}\n---")

            st.subheader("🧠 Synthesized Theme Summary")
            st.markdown(data["theme_summary"])
        else:
            st.error("❌ Query failed. Likely due to API key quota or backend issue.")
