from pydantic import BaseModel, Field
from datetime import datetime
from typing import List

class ChatMessage(BaseModel):
    role: str  # "user" or "assistant"
    content: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)

class ChatRequest(BaseModel):
    message: str

class ResponseChat(BaseModel):
    response: str
    history: List[ChatMessage] = [] # Optional: return history in response