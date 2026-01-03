from fastapi import APIRouter, HTTPException
from app.models.chat import ChatRequest, ResponseChat, ChatMessage
from app.services.chat_service import ChatService
from app.services.agent import run_agent

router = APIRouter()

@router.post("/chat/{session_id}", response_model=ResponseChat)
async def chat_with_agent(session_id: str, request: ChatRequest):
    
    # Save user message
    user_msg = ChatMessage(role="user", content=request.message)
    await ChatService.add_message_to_history(session_id, user_msg)

    # Get history for the Agent context
    history = await ChatService.get_history(session_id)
    agent_response_text = await run_agent(message=request.message)

    if not agent_response_text:
        raise HTTPException(status_code=500, detail="Internal Error, try again later!")
    
    # Save agent response
    agent_msg = ChatMessage(role="assistant", content=agent_response_text)
    await ChatService.add_message_to_history(session_id, agent_msg)
    
    return ResponseChat(
        response=agent_response_text,
        history=history + [agent_msg]
    )