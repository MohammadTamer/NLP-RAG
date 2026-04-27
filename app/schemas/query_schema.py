from pydantic import BaseModel
from typing import List


class QueryRequest(BaseModel):
    question: str


class Source(BaseModel):
    text: str
    filename: str
    score: float


class QueryResponse(BaseModel):
    question: str
    answer: str
    sources: List[Source]