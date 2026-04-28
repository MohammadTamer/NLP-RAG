from fastapi import APIRouter
from app.services.retrieval_service import retrieve_chunks
from app.services.llm_service import generate_answer
from app.schemas.query_schema import QueryRequest, QueryResponse, Source

router = APIRouter()


@router.post("/query", response_model=QueryResponse)
def query(request: QueryRequest):
    retrieved = retrieve_chunks(request.question)

    contexts = []
    for r in retrieved:
        contexts.append(r["text"])

    answer = generate_answer(request.question, contexts, model_name=request.model)

    sources = []

    for r in retrieved:
        obj = Source(
            text=r["text"],
            filename=r["filename"],
            score=r["score"]
        )
        sources.append(obj)

    return QueryResponse(
        question=request.question,
        answer=answer,
        sources=sources
    )
