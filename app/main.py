from fastapi import FastAPI
from app.chat.chat import router
from app.core.config import settings
from app.core.event import lifespan

app = FastAPI(
    title="Simple Agent Service",
    description="Simple_For_Question_Answer",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host=settings.APP_HOST,
        port=settings.APP_PORT,
        reload=True
    )