from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./data/app_data.db"
    REPLICATE_API_TOKEN: str
    MODEL_VERSION: str

    class Config:
        env_file = ".env"

settings = Settings()
