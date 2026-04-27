from fastapi import APIRouter, UploadFile, File
import os

from app.services.file_service import extract_text_from_pdf
from app.services.cleaning import clean_text
from app.services.chunking_service import chunk_text
from app.services.embedding_service import get_embeddings
from app.services.vector_db_service import store_chunks

from app.schemas.ingest_schema import IngestResponse

router = APIRouter()

UPLOAD_DIR = "uploads/"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/ingest", response_model=IngestResponse)
async def ingest(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    extracted_text = extract_text_from_pdf(file_path)
    cleaned_text = clean_text(extracted_text)
    chunks = chunk_text(cleaned_text)
    embeddings = get_embeddings(chunks)

    store_chunks(chunks, embeddings, file.filename)

    return IngestResponse(
        message="file processed and stored successfully",
        filename=file.filename,
        chunks_count=len(chunks)
    )