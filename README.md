# 📘 RAG Project Plan — Full Detailed Version

---

## 🚀 1) Project Overview

This project is a **Retrieval-Augmented Generation (RAG)** system that answers user questions using unstructured documents.

### 🔄 System Workflow:
1. 📥 Ingest raw PDF files  
2. 🧹 Extract and clean text  
3. ✂️ Split text into chunks  
4. 🔢 Convert chunks into embeddings  
5. 🗄️ Store in vector database  
6. 🔍 Retrieve relevant chunks  
7. 🤖 Generate answers using LLM  

🎯 **Goal:** Build a complete backend system (not just a notebook)

---

## 💡 2) Why This Project

- ✅ Easier than building a custom Transformer  
- 🧠 Focuses on engineering instead of deep ML  
- 🌍 Uses real-world data  
- 📋 Matches assignment requirements  

---

## 📂 3) Project Idea

Use **PDF documents in ONE domain**:

- 🎓 University regulations ✅ (Best choice)
- 🏢 HR policies  
- 📘 Company manuals  
- 📦 Product documentation  

---

## ⚙️ 4) System Capabilities

The system should:

- 📥 Ingest raw PDFs  
- 🧹 Process messy text  
- 🧠 Store embeddings  
- 🔍 Retrieve relevant context  
- 🤖 Answer questions via API  

---

## 🧰 5) Tech Stack

### 🧹 Data Processing
- PyMuPDF / pdfplumber  
- regex cleaning  

### 🧠 Embeddings
- sentence-transformers  

### 🗄️ Vector DB
- ChromaDB / FAISS  

### 🌐 Backend
- FastAPI  

### 🐳 Deployment
- Docker + docker-compose  

### 🤖 LLM
- Ollama or API  

---

## 🗂️ 6) Project Structure

```bash
project/
├── app/
│   ├── main.py
│   ├── routers/
│   ├── services/
│   ├── schemas/
│   └── utils/
├── data/
├── vectordb/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md

# 📊 7) Data Collection Plan

## 📥 Input Data

* Collect **5 → 10 PDF files** in the same domain

## 📌 Requirements

* Raw PDFs
* Not pre-cleaned
* Not CSV files
* Multi-page documents

## 🏷️ Metadata to Store

* file name
* page number
* chunk ID
* document title

---

# 🧼 8) Data Extraction & Cleaning

## 🔄 Steps

1. Extract text page by page
2. Remove spacing issues
3. Normalize whitespace
4. Remove noise
5. Preserve structure

## 🧪 Cleaning Examples

* Remove extra spaces
* Fix line breaks
* Remove repeated headers
* Keep paragraphs

## 🎯 Importance

✨ Better cleaning = Better retrieval = Better answers

---

# ✂️ 9) Chunking Strategy

## ⚙️ Settings

* Chunk size: **400–500 tokens**
* Overlap: **50 tokens**

## 🤔 Why?

* Small chunks → lose context ❌
* Large chunks → add noise ❌
* Overlap → preserves meaning ✅

## 🚀 Improvement

Use **sentence-based chunking** instead of random splitting

---

# 🔢 10) Embedding & Vectorization

## 🔄 What Happens

Each chunk → vector representation

## 🧰 Tools

* sentence-transformers

## 💾 Stored Data

* embedding
* text
* metadata

## 🎯 Benefit

✨ Semantic search instead of keyword matching

---

# 🔍 11) Retrieval Pipeline

## 🔄 Flow

1. User sends question
2. Convert to embedding
3. Search vector DB
4. Get top-k chunks
5. Send to LLM
6. Generate answer

## ⚙️ Recommended

* `top_k = 3 or 5`

---

# 🌐 12) FastAPI Backend Design

## 📥 POST /ingest

Process documents and store embeddings

```json
{
  "message": "Documents ingested successfully",
  "files_processed": 5,
  "chunks_created": 48
}
```

---

## ❓ POST /query

```json
{
  "question": "What is the attendance policy?"
}
```

## 📤 Response

```json
{
  "question": "What is the attendance policy?",
  "answer": "...",
  "sources": [
    {
      "file_name": "handbook.pdf",
      "page": 12,
      "chunk_id": "chunk_14"
    }
  ]
}
```

---

## ❤️ GET /health

Check API status

---

# 🐳 13) Docker & Deployment

## 📦 Required

* Dockerfile
* docker-compose.yml

## ▶️ Run Command

```bash
docker-compose up
```

## 🧩 Services

* FastAPI
* Vector DB

---

# 📈 14) Evaluation Plan

## ✅ Successful Cases

* Attendance policy
* Graduation requirements
* Deadlines

## ❌ Failure Cases

* Wrong chunk retrieved
* Hallucination
* Vague question
* Missing context

## 🔍 Analysis

Explain:

* What failed
* Why
* How to fix

---

# 📄 15) Technical Report

## 🧾 Sections

* Executive Summary
* Problem Statement
* Data Source
* Cleaning
* Chunking
* Embeddings
* Vector DB
* API
* Docker
* Evaluation
* Errors
* Conclusion

---

# ⚠️ 16) What to Avoid

* ❌ Scanned PDFs
* ❌ Too much data
* ❌ Over-engineering
* ❌ Bonus features early

---

# ⏳ 17) Timeline

## 📅 Day 1

* Choose topic
* Collect data

## 📅 Day 2

* Extraction + cleaning

## 📅 Day 3

* Chunking + embeddings

## 📅 Day 4

* FastAPI

## 📅 Day 5

* Connect LLM

## 📅 Day 6

* Evaluation

## 📅 Day 7

* Docker + final report

---

# 🎯 18) Final Goal

Build a system that:

* 📥 Processes PDFs
* 🔍 Retrieves knowledge
* 🤖 Answers questions
* 🐳 Runs with Docker
* 🌐 Exposes API

---

# 💬 19) Final Advice

✨ Keep it simple.

## 🧠 Best Strategy:

* One domain
* Few PDFs
* Clean pipeline
* Working API
* Clear evaluation
