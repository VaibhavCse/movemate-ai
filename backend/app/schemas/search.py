from typing import Any

from pydantic import BaseModel, Field


class SearchResult(BaseModel):
    """
    Represents a single search result.
    """

    title: str = Field(..., description="Title of the search result")

    url: str = Field(..., description="Source URL")

    content: str = Field(..., description="Content/snippet")

    score: float | None = Field(
        default=None,
        description="Provider relevance score",
    )

    metadata: dict[str, Any] = Field(
        default_factory=dict,
        description="Additional provider-specific metadata",
    )


class SearchResponse(BaseModel):
    """
    Standardized response returned by every search provider.
    """

    query: str = Field(..., description="Original search query")

    provider: str = Field(..., description="Search provider name")

    results: list[SearchResult] = Field(
        default_factory=list,
        description="Search results",
    )

    total_results: int = Field(
        default=0,
        description="Number of results returned",
    )