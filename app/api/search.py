from fastapi import APIRouter
from pydantic import BaseModel

from app.rag.query import ask_rag

router = APIRouter(
    prefix="/rag",
    tags=["RAG"]
)


class QueryRequest(BaseModel):
    question: str


@router.post("/ask")
def ask(request: QueryRequest):

    answer = ask_rag(request.question)

    return {
        "answer": answer
    }