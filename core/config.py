from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """
    Application settings.
    """
    DATABASE_URL: str
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 8 days
    ALGORITHM: str = "HS256"

    class Config:
        env_file = ".env"

settings = Settings()
