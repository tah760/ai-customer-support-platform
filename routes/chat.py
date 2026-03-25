from fastapi import APIRouter
from pydantic import BaseModel
from services.llm_service import get_ai_response

router = APIRouter(prefix="/chat")

class ChatRequest(BaseModel):
    message: str

@router.post("/")
async def chat(req: ChatRequest):
    response = get_ai_response(req.message)
    return {"response": response}
