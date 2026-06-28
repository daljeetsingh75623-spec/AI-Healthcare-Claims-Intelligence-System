from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    NVIDIA_API_KEY: str
    BASE_URL: str
    MODEL_NAME: str

    APP_NAME: str = "AI Healthcare Claims Intelligence System"

    class Config:
        env_file = ".env"


settings = Settings()