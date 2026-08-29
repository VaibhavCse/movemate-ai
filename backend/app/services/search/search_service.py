from typing import Any

from app.clients.search import BaseSearchProvider
from app.core.logger import logger
from app.schemas.search import SearchResponse


class SearchService:
    """
    Service responsible for orchestrating web searches.

    This service is provider-agnostic and delegates
    search execution to the configured provider.
    """

    def __init__(self, provider: BaseSearchProvider):
        self.provider = provider

    async def search(
        self,
        query: str,
        **kwargs: Any,
    ) -> SearchResponse:
        """
        Execute a web search.

        Args:
            query: Search query.
            **kwargs: Provider-specific options.

        Returns:
            SearchResponse
        """

        query = query.strip()

        if not query:
            raise ValueError("Search query cannot be empty.")

        logger.info(f"Searching: {query}")

        response = await self.provider.search(
            query=query,
            **kwargs,
        )

        logger.info(
            "Search completed successfully "
            f"({response.total_results} results)"
        )

        return response