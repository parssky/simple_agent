from app.db.redis import redis_db
from typing import List
from app.models.chat import ChatMessage

class ChatService:
    @staticmethod
    async def add_message_to_history(session_id: str, message: ChatMessage):
        """Appends a message to the Redis list as a JSON string."""
        key = f"chat_history:{session_id}"
        # .model_dump_json() is the Pydantic v2 way to serialize
        await redis_db.client.rpush(key, message.model_dump_json())
        # Optional: Keep only the last 50 messages to save memory
        await redis_db.client.ltrim(key, -50, -1)
        # Set expiry for 24 hours
        await redis_db.client.expire(key, 86400)

    @staticmethod
    async def get_history(session_id: str) -> List[ChatMessage]:
        """Retrieves and parses the chat history."""
        key = f"chat_history:{session_id}"
        raw_messages = await redis_db.client.lrange(key, 0, -1)
        
        return [ChatMessage.model_validate_json(m) for m in raw_messages]