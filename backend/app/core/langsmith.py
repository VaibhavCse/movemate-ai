import os

from app.core.config import settings


def configure_langsmith() -> None:
    """
    Configure LangSmith environment variables before any LangChain
    components are initialized.
    """

    os.environ["LANGSMITH_TRACING"] = (
        str(settings.LANGSMITH_TRACING).lower()
    )

    os.environ["LANGSMITH_API_KEY"] = settings.LANGSMITH_API_KEY

    os.environ["LANGSMITH_PROJECT"] = settings.LANGSMITH_PROJECT

    os.environ["LANGSMITH_ENDPOINT"] = "https://api.smith.langchain.com"