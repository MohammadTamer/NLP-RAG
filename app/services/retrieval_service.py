from sentence_transformers import SentenceTransformer
from app.services.vector_db_service import client, COLLECTION_NAME

model = SentenceTransformer("all-MiniLM-L6-v2")

def retrieve_chunks(query: str, top_k=5):
    query_vector = model.encode(query).tolist()
    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_vector,
        limit=top_k
    ).points

    return [
        {
            "text": r.payload["text"],
            "filename": r.payload["filename"],
            "score": r.score
        }
        for r in results
    ]