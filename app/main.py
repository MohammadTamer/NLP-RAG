from fastapi import FastAPI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import routers
from app.api.routes import ingest
from app.services.vector_db_service import create_collection

app = FastAPI(title="RAG System API")

# Include routers
app.include_router(ingest.router)

# Root endpoint
@app.get("/")
def root():
    return {"message": "RAG system is running"}

# Health check
@app.get("/health")
def health():
    return {"status": "ok"}

@app.on_event("startup")
def startup_event():
    create_collection()