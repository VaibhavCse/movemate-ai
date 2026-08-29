from app.clients.search import TavilyProvider
from app.services.search.search_service import SearchService


def get_search_service() -> SearchService:
    return SearchService(
        provider=TavilyProvider(),
    )