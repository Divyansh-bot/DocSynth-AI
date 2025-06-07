# DocSynth AI (Cloud Version)

**DocSynth AI** is an AI-powered document research assistant that allows users to upload PDF documents or scanned images, ask natural language questions, and receive accurate answers with source citations. It also synthesizes themes across multiple documents using OpenAI's GPT models.

This version uses **OpenAI APIs** for embeddings and theme summarization and is designed to showcase semantic document understanding for the Wasserstoff AI Internship Task.

---

## 🚀 Features

- 📤 Upload PDFs, scanned documents, or images
- 🔡 Extract text using OCR (`Tesseract`) and PDF parsing (`PyMuPDF`)
- 🧠 Embedding-based semantic search via `OpenAI text-embedding-ada-002`
- 🔍 Retrieve answers with page-level citations
- 🧩 Summarize themes using GPT-3.5 (`gpt-3.5-turbo`)
- 🧱 Modular backend (FastAPI) and frontend (Streamlit)
- ✅ Clean, testable codebase ready for deployment

---

## 🛠 Tech Stack

| Component | Tool |
|----------|------|
| Frontend | Streamlit |
| Backend | FastAPI |
| Embedding | OpenAI `text-embedding-ada-002` |
| LLM | OpenAI `gpt-3.5-turbo` |
| OCR | Tesseract |
| PDF Parsing | PyMuPDF |
| Vector DB | ChromaDB |

---

## 📦 Project Structure

```
docsynth-ai/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── services/
│   │   ├── utils/
│   │   ├── main.py
│   │   └── config.py
│   ├── .env.example
│   ├── requirements.txt
├── frontend/
│   └── app.py
├── data/
└── README.md
```

---

## 🔧 How to Use

### 1. Setup Environment

```bash
pip install -r backend/requirements.txt
pip install streamlit
```

### 2. Add Your OpenAI API Key

Create a `.env` file in `/backend/` with:

```
OPENAI_API_KEY=sk-xxxxxx
```

### 3. Run Backend

```bash
cd backend
python -m uvicorn app.main:app --reload
```

### 4. Run Frontend

```bash
cd frontend
streamlit run app.py
```

---

## 📄 Example Use Case

- Upload 5+ documents
- Ask: “What penalties were imposed?”
- Get:
  - A table of answers with citations
  - Synthesized theme summary using GPT

---


