from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.db.redis import redis_db



@asynccontextmanager
async def lifespan(app: FastAPI):
    
    # Start
    redis_db.connect()  
    print("Redis connected.")
    yield 
    
    # Shutdown
    redis_db.close()
    print("Shutdown complete")