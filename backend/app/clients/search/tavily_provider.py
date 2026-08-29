from typing import Any

import httpx

from app.clients.search.base_provider import BaseSearchProvider
from app.core.config import settings
from app.core.exceptions import SearchProviderError
from app.schemas.search import SearchResponse, SearchResult


class TavilyProvider(BaseSearchProvider):
    """
    Tavily Search Provider.
    Responsible for communicating with the Tavily Search API.
    """

    BASE_URL = "https://api.tavily.com/search"

    async def search(
        self,
        query: str,
        **kwargs: Any,
    ) -> SearchResponse:

        payload = {
            "api_key": settings.TAVILY_API_KEY,
            "query": query,
            "search_depth": kwargs.get("search_depth", "advanced"),
            "max_results": kwargs.get("max_results", 5),
            "include_answer": False,
            "include_images": False,
        }

        timeout = httpx.Timeout(settings.REQUEST_TIMEOUT)

        try:
            async with httpx.AsyncClient(timeout=timeout) as client:

                response = await client.post(
                    self.BASE_URL,
                    json=payload,
                )

                response.raise_for_status()

                data = response.json()

        except httpx.HTTPStatusError as exc:
            raise SearchProviderError(
                f"Tavily API returned {exc.response.status_code}"
            ) from exc

        except httpx.RequestError as exc:
            raise SearchProviderError(
                "Unable to connect to Tavily."
            ) from exc

        results = []

        for item in data.get("results", []):

            results.append(
                SearchResult(
                    title=item.get("title", ""),
                    url=item.get("url", ""),
                    content=item.get("content", ""),
                    score=item.get("score"),
                    metadata={
                        "raw": item,
                    },
                )
            )

        return SearchResponse(
            query=query,
            provider="tavily",
            results=results,
            total_results=len(results),
        )