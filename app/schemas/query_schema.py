from pydantic import BaseModel
from typing import List, Optional


class QueryRequest(BaseModel):
    question: str
    provider: Optional[str] = None  # "ollama", "gemini"
    model: Optional[str] = None     # "llama3", "gemini-1.5-pro"

class Source(BaseModel):
    text: str
    filename: str
    score: float


class QueryResponse(BaseModel):
    question: str
    answer: str
    sources: List[Source]