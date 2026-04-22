# 📘 Simple RAG Project Plan

## 🎯 Project Idea
Build a Retrieval-Augmented Generation (RAG) system using **unstructured PDF documents** in a single domain  
(e.g., HR policies, university regulations, or product manuals).

---

## 🧠 Why This Idea?
- Easy to implement  
- Meets all project constraints  
- Focus on engineering instead of heavy ML  

---

## 🧰 Tech Stack
- **Parsing**: PyMuPDF / pdfplumber  
- **Chunking**: 400–500 tokens with 50 overlap  
- **Embeddings**: sentence-transformers  
- **Vector DB**: ChromaDB or FAISS  
- **Backend**: FastAPI  
- **LLM**: Ollama or API  
- **Deployment**: Docker + docker-compose  

---

## 🏗️ Project Structure
```bash
project/
├── app/
│   ├── main.py
│   ├── routers/
│   ├── services/
│   ├── models/
│   └── utils/
├── data/
├── chroma_db/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
