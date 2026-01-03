import redis.asyncio as redis
from app.core.config import settings

class RedisDatabase:
    def __init__(self) -> None:
        self.client: redis.Redis = None
    
    def connect(self):
        self.client = redis.from_url(
            settings.REDIS_URI,
            encoding = "utf-8",
            decode_responses=True
        )
        print("Connected to Redis")
    

    async def close(self):
        if self.client:
            await self.client.aclose()
            print("Redis connection closed")


redis_db = RedisDatabase()