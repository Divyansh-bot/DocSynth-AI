from fastapi import APIRouter, File, UploadFile
import shutil
import os

from app.services.ocr_service import extract_text_from_pdf, extract_text_from_image
from app.services.embedding_service import store_document_embedding
from app.config import UPLOAD_FOLDER
from app.utils.text_splitter import chunk_text

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    # Save uploaded file
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract text from file
    if file.filename.lower().endswith(".pdf"):
        text = extract_text_from_pdf(filepath)
    elif file.filename.lower().endswith((".png", ".jpg", ".jpeg")):
        text = extract_text_from_image(filepath)
    else:
        return {"error": "Unsupported file type. Upload PDF or image only."}

    if not text.strip():
        return {"error": "No readable text extracted from file."}

    # Chunk and store embeddings
    chunks = chunk_text(text)
    store_document_embedding(file.filename, chunks)

    return {
        "filename": file.filename,
        "chunks_uploaded": len(chunks),
        "message": "File processed and stored successfully."
    }
