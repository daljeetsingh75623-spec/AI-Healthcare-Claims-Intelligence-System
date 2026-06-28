from fastapi import APIRouter

from app.models.schemas import ChatRequest
from app.models.schemas import ChatResponse

from app.services.chat_service import process_chat


router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    answer = process_chat(request.message)

    return ChatResponse(response=answer)