from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

from app.routes import ingest, query, reset
from app.services.vector_db_service import create_collection

app = FastAPI(title="RAG System API")

app.include_router(ingest.router)
app.include_router(query.router)
app.include_router(reset.router)

@app.get("/")
def root():
    return {"message": "RAG system is running"}


@app.on_event("startup")
def startup_event():
    create_collection()
