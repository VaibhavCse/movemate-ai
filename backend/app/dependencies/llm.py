from app.clients.llm import GeminiProvider
from app.services.llm.summarizer_service import SummarizerService


def get_summarizer_service() -> SummarizerService:
    return SummarizerService(
        provider=GeminiProvider(),
    )