# 📘 RAG Project Plan — Detailed Version

## 1) Project Overview

This project is a **Retrieval-Augmented Generation (RAG)** system built to answer questions from a collection of raw, unstructured documents.

The main idea is simple:
- ingest real documents,
- extract and clean the text,
- split the content into meaningful chunks,
- convert the chunks into embeddings,
- store them in a vector database,
- retrieve the most relevant chunks for each query,
- generate an answer using an LLM.

The goal is to build a **complete working backend pipeline**, not just a notebook demo.

---

## 2) Why This Project Is the Easiest Option

This project is easier than the Transformer research project because:
- it relies more on **system design and integration** than deep model training,
- most of the hard NLP parts are already available as tools or libraries,
- you do not need to train a custom neural architecture from scratch,
- you can focus on engineering, retrieval, and deployment.

It is still a strong project because it matches the required rules:
- use raw, messy documents,
- process the data yourself,
- justify chunking,
- build a FastAPI backend,
- containerize everything with Docker,
- evaluate retrieval quality and failure cases. :contentReference[oaicite:1]{index=1}

---

## 3) Recommended Project Topic

Choose **one domain only** so the project stays clean and manageable.

Good examples:
- university regulations and student handbook,
- HR policies,
- company internal policies,
- product manuals,
- legal or administrative manuals.

Best choice for simplicity:
**University handbook / regulations PDF documents**

Why?
- the content is structured enough to retrieve from,
- the documents are easy to gather,
- the language is clear,
- the data is still “raw” and unstructured enough to satisfy the assignment.

---

## 4) What the Final System Will Do

The final system should:
1. accept raw PDF documents,
2. extract and clean the text,
3. split the text into chunks,
4. store chunks with metadata in a vector database,
5. receive a user question,
6. retrieve relevant chunks,
7. send those chunks to an LLM,
8. return the final answer through an API.

---

## 5) Suggested Tech Stack

### Data Processing
- PyMuPDF (`fitz`)
- pdfplumber
- regex for cleaning
- pandas for metadata handling if needed

### Embeddings
- `sentence-transformers`
- a lightweight sentence embedding model

### Vector Database
- ChromaDB
- or FAISS if you want a very simple local setup

### Backend
- FastAPI
- Pydantic models
- Uvicorn

### Deployment
- Docker
- docker-compose

### LLM
- Ollama local model
- or an API-based model if allowed

---

## 6) Project Folder Structure

```bash
project/
├── app/
│   ├── main.py
│   ├── routers/
│   │   ├── ingest.py
│   │   └── query.py
│   ├── services/
│   │   ├── parser_service.py
│   │   ├── chunking_service.py
│   │   ├── embedding_service.py
│   │   ├── retrieval_service.py
│   │   └── generation_service.py
│   ├── models/
│   │   └── schemas.py
│   └── utils/
│       └── text_cleaning.py
├── data/
│   ├── raw/
│   └── processed/
├── vectordb/
├── tests/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
