from pydantic import BaseModel
from typing import List, Optional


class QueryRequest(BaseModel):
    question: str
    provider: Optional[str] = None  # e.g., "ollama", "openai", "gemini"
    model: Optional[str] = None     # e.g., "llama3", "gpt-3.5-turbo"

class Source(BaseModel):
    text: str
    filename: str
    score: float


class QueryResponse(BaseModel):
    question: str
    answer: str
    sources: List[Source]