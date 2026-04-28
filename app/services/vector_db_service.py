import os
from qdrant_client import QdrantClient
from qdrant_client.http import models

QDRANT_HOST = os.getenv("QDRANT_HOST", "localhost")
QDRANT_PORT = int(os.getenv("QDRANT_PORT", 6333))
client = QdrantClient(host=QDRANT_HOST, port=QDRANT_PORT)
COLLECTION_NAME = "rag_chunks"


def create_collection(vector_size: int = 384):
    collections = client.get_collections().collections
    existing_names = [c.name for c in collections]

    if COLLECTION_NAME not in existing_names:
        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=models.VectorParams(
                size=vector_size,
                distance=models.Distance.COSINE
            )
        )


def store_chunks(chunks, embeddings, filename):
    points = []

    for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
        points.append(
            models.PointStruct(
                id=i,
                vector=embedding,
                payload={
                    "text": chunk,
                    "filename": filename,
                    "chunk_id": f"chunk_{i}"
                }
            )
        )
    client.upsert(
        collection_name=COLLECTION_NAME,
        points=points
    )


def delete_collection():
    client.delete_collection(collection_name=COLLECTION_NAME)
