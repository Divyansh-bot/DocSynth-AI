from fastapi import FastAPI
from app.api.upload import router as upload_router
from app.api.query import router as query_router

app = FastAPI(title="DocuMind AI - Backend")

# Include routes
app.include_router(upload_router, prefix="/api", tags=["Upload"])
app.include_router(query_router, prefix="/api", tags=["Query"])

@app.get("/")
def root():
    return {"message": "Welcome to DocuMind AI backend"}
