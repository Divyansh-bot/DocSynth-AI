from fastapi import APIRouter
from pydantic import BaseModel
from app.services.query_service import query_documents
from app.services.summarize_service import generate_theme_summary

router = APIRouter()

class QueryRequest(BaseModel):
    question: str

@router.post("/query")
def ask_question(data: QueryRequest):
    chunks = query_documents(data.question)
    summary = generate_theme_summary(data.question, chunks)
    return {
        "document_matches": chunks,
        "theme_summary": summary
    }
