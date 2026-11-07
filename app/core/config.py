from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    APP_NAME: str = "AI Video Creator"

    APP_ENV: str = "development"

    APP_HOST: str = "127.0.0.1"

    APP_PORT: int = 8000

    UPLOAD_DIR: str = "uploads"

    OUTPUT_DIR: str = "outputs"

    class Config:
        env_file = ".env"


settings = Settings()