from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # App
    APP_HOST: str
    APP_PORT: int
    
    # API
    API_KEY: str
    BASE_URL: str

    # DB
    REDIS_URI: str = "redis://redis:6379"


    class Config:
        env_file =".env"

settings = Settings()