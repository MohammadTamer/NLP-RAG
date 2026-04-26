from qdrant_client import QdrantClient
from qdrant_client.http import models

client = QdrantClient(host="localhost", port=6333)
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
