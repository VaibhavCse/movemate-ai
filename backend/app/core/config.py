from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application configuration loaded from environment variables.
    """

    # -------------------------------------------------------------------------
    # Application
    # -------------------------------------------------------------------------

    APP_NAME: str = "MoveMate AI Backend"
    APP_VERSION: str = "1.0.0"
    APP_DESCRIPTION: str = "AI-powered relocation assistant backend"

    API_PREFIX: str = "/api/v1"

    DEBUG: bool = True

    LOG_LEVEL: str = "INFO"

    # -------------------------------------------------------------------------
    # AI Providers
    # -------------------------------------------------------------------------

    GOOGLE_API_KEY: str = Field(
        ...,
        description="Google Gemini API Key",
    )

    # -------------------------------------------------------------------------
    # Search Providers
    # -------------------------------------------------------------------------

    TAVILY_API_KEY: str = Field(
        default="",
        description="Tavily Search API Key",
    )

    # -------------------------------------------------------------------------
    # LangSmith
    # -------------------------------------------------------------------------

    LANGSMITH_API_KEY: str = Field(
        ...,
        description="LangSmith API Key",
    )

    LANGSMITH_TRACING: bool = False

    LANGSMITH_PROJECT: str = "MoveMate-AI"

    # -------------------------------------------------------------------------
    # HTTP Client
    # -------------------------------------------------------------------------

    REQUEST_TIMEOUT: int = 30

    # -------------------------------------------------------------------------
    # Configuration
    # -------------------------------------------------------------------------

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    """
    Returns cached application settings.
    """
    return Settings()


settings = get_settings()