from sentence_transformers import SentenceTransformer

model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

def get_embeddings(chunks):
    embeddings = model.encode(chunks)
    return embeddings.tolist()