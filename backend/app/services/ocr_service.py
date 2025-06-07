import pytesseract
from PIL import Image
import fitz  # PyMuPDF
import os

def extract_text_from_pdf(path):
    text = ""
    doc = fitz.open(path)
    for page in doc:
        text += page.get_text()
    return text

def extract_text_from_image(path):
    img = Image.open(path)
    text = pytesseract.image_to_string(img)
    return text
