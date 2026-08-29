from abc import ABC, abstractmethod
from typing import Any

from app.schemas.search import SearchResponse


class BaseSearchProvider(ABC):
    """
    Abstract base class for all search providers.

    Every search provider (Tavily, SerpAPI, Brave Search, etc.)
    must implement this interface.
    """

    @abstractmethod
    async def search(
        self,
        query: str,
        **kwargs: Any,
    ) -> SearchResponse:
        """
        Execute a web search.

        Args:
            query: User search query.

        Returns:
            Standardized SearchResponse.
        """
        raise NotImplementedError