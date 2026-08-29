from app.ai.chains.apartment_extraction import ApartmentExtractionChain
from app.clients.llm.gemini_provider import GeminiProvider
from app.dependencies.llm import get_summarizer_service
from app.dependencies.search import get_search_service
from app.services.housing.apartment_service import ApartmentService


def get_gemini_provider() -> GeminiProvider:
    """
    Returns the shared Gemini provider.
    """
    return GeminiProvider()


def get_apartment_extraction_chain() -> ApartmentExtractionChain:
    """
    Returns the apartment extraction AI chain.
    """
    return ApartmentExtractionChain(
        provider=get_gemini_provider(),
    )


def get_apartment_service() -> ApartmentService:
    """
    Returns the apartment service.
    """
    return ApartmentService(
        search_service=get_search_service(),
        summarizer=get_summarizer_service(),
        extraction_chain=get_apartment_extraction_chain(),
    )