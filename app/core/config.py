from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    OPENAI_API_KEY: str = ""
    APP_ENV: str = "development"
    DEBUG: bool = True

    UPLOAD_DIR: str = "data/uploads"

    MAX_FILE_SIZE: int = 50 * 1024 * 1024

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

settings=Settings()        