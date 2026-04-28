from pydantic import BaseModel
from typing import List, Optional


class QueryRequest(BaseModel):
    question: str
    model: Optional[str] = "llama3"

class Source(BaseModel):
    text: str
    filename: str
    score: float


class QueryResponse(BaseModel):
    question: str
    answer: str
    sources: List[Source]