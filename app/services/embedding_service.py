from sentence_transformers import SentenceTransformer

# Changed to a multilingual model to support Arabic queries and documents properly.
model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

def get_embeddings(chunks):
    embeddings = model.encode(chunks)
    return embeddings.tolist()