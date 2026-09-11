import re

from app.ai.chains.apartment_extraction import ApartmentExtractionChain
from app.schemas.apartment import ApartmentListing, ApartmentSearchResponse
from app.schemas.search import SearchResponse
from app.services.llm.summarizer_service import SummarizerService
from app.services.search.search_service import SearchService


class ApartmentService:
    """
    Service responsible for apartment-related search operations.

    Apartment search and nearby gym discovery are intentionally handled
    as separate searches:

    1. One Tavily search for apartments.
    2. One area-level Tavily search for gyms, only when requested.

    Gym search is not performed separately for each apartment listing.
    """

    # Generic words that do not provide useful location relevance.
    LOCATION_STOP_WORDS = {
        "apartment",
        "apartments",
        "area",
        "bangalore",
        "bengaluru",
        "city",
        "flat",
        "flats",
        "layout",
        "locality",
        "main",
        "near",
        "office",
        "road",
        "rent",
        "rental",
        "street",
    }

    def __init__(
        self,
        search_service: SearchService,
        summarizer: SummarizerService,
        extraction_chain: ApartmentExtractionChain,
    ):
        self.search_service = search_service
        self.summarizer = summarizer
        self.extraction_chain = extraction_chain

    async def search_apartments(
        self,
        location: str,
        budget: int | None = None,
        apartment_type: str | None = None,
        furnished: bool | None = None,
        parking: bool | None = None,
        brokerage: bool | None = None,
        gym_required: bool = False,
        gym_type: str | None = None,
    ) -> ApartmentSearchResponse:
        """
        Search apartments and optionally search for nearby gyms.

        Apartment search always performs one apartment search.

        Gym search is performed only when gym_required=True and is an
        area-level search rather than a separate search for every apartment.
        """

        # ---------------------------------------------------------
        # Apartment search
        # ---------------------------------------------------------

        query = self._build_search_query(
            location=location,
            budget=budget,
            apartment_type=apartment_type,
            furnished=furnished,
            parking=parking,
            brokerage=brokerage,
        )

        search_response = await self.search_service.search(
            query=query,
            max_results=5,
        )

        content = self._format_results(search_response)

        extraction = await self.extraction_chain.invoke(
            content=content,
        )

        listings = self._filter_listings(
            listings=extraction.listings,
            location=location,
            budget=budget,
            apartment_type=apartment_type,
            furnished=furnished,
            parking=parking,
            brokerage=brokerage,
        )

        listings = self._rank_listings(
            listings=listings,
            requested_location=location,
        )

        summary = self._build_summary(listings)

        # ---------------------------------------------------------
        # Optional area-level gym search
        # ---------------------------------------------------------

        nearby_places = []

        if gym_required:
            nearby_places = await self._search_nearby_gyms(
                location=location,
                gym_type=gym_type,
            )

        # ---------------------------------------------------------
        # Build response
        # ---------------------------------------------------------

        return ApartmentSearchResponse(
            summary=summary,
            total_results=len(listings),
            listings=listings,
            nearby_places=nearby_places,
        )

    @staticmethod
    def _build_summary(
        listings: list[ApartmentListing],
    ) -> str:
        """
        Build a deterministic apartment search summary.

        This avoids an additional Gemini call merely to summarize
        the apartment search results.
        """

        if not listings:
            return "No listings matched the requested criteria."

        return (
            f"Found {len(listings)} apartment"
            f"{'s' if len(listings) != 1 else ''} "
            "matching your requested criteria."
        )

    def _build_search_query(
        self,
        location: str,
        budget: int | None,
        apartment_type: str | None,
        furnished: bool | None,
        parking: bool | None,
        brokerage: bool | None,
    ) -> str:
        """
        Build the Tavily query for apartment discovery.
        """

        parts = []

        if apartment_type:
            parts.append(apartment_type)

        parts.append("apartment")
        parts.append(location)

        if budget:
            parts.append(f"under ₹{budget}")

        if furnished is True:
            parts.append("furnished")

        elif furnished is False:
            parts.append("unfurnished")

        if parking is True:
            parts.append("parking")

        if brokerage is False:
            parts.append("without broker")

        elif brokerage is True:
            parts.append("broker listings")

        parts.append("rent")

        return " ".join(parts)

    def _build_gym_search_query(
        self,
        location: str,
        gym_type: str | None = None,
    ) -> str:
        """
        Build an area-level gym search query.

        The query intentionally searches the requested area as a whole
        instead of searching around each apartment individually.
        """

        normalized_location = location.strip()

        # ---------------------------------------------------------
        # Cult-specific search
        # ---------------------------------------------------------

        if gym_type == "cult":
            return (
                f"Cult.fit gyms fitness centers near "
                f"{normalized_location} Bangalore"
            )

        return (
            f"gyms fitness centers near "
            f"{normalized_location} Bangalore"
        )

        # ---------------------------------------------------------
        # General gym search
        # ---------------------------------------------------------

        return (
            f"gyms fitness centers near "
            f"{normalized_location} Bangalore"
        )

    async def _search_nearby_gyms(
        self,
        location: str,
        gym_type: str | None = None,
    ) -> list[dict]:
        """
        Perform ONE area-level Tavily search for nearby gyms.

        This method does not perform a search for every apartment.

        The raw Tavily results are returned separately from apartment
        listings because Tavily search results do not provide reliable
        apartment-to-gym distance information.

        The returned data is intentionally limited to the information
        supplied by Tavily.
        """

        query = self._build_gym_search_query(
            location=location,
            gym_type=gym_type,
        )

        try:
            search_response = await self.search_service.search(
                query=query,
                max_results=6,
            )

        except Exception:
            # Gym discovery is an optional enhancement.

            # If the gym search fails, the apartment search should
            # still succeed normally.
            return []

        nearby_places = []

        for result in search_response.results:
            nearby_places.append(
                {
                    "name": result.title,
                    "url": result.url,
                    "description": result.content,
                    "source": "Tavily",
                }
            )

        return nearby_places

    @classmethod
    def _normalize_location(cls, value: str) -> set[str]:
        """
        Convert a location string into meaningful searchable terms.

        Generic location words such as 'road', 'layout', and 'office'
        are ignored because they do not help determine geographic
        relevance.
        """

        normalized = value.lower().strip()

        # Treat Bangalore and Bengaluru as the same city.
        normalized = normalized.replace(
            "bengaluru",
            "bangalore",
        )

        # Replace punctuation with spaces.
        normalized = re.sub(
            r"[^a-z0-9]+",
            " ",
            normalized,
        )

        tokens = normalized.split()

        return {
            token
            for token in tokens
            if token not in cls.LOCATION_STOP_WORDS
            and len(token) > 2
        }

    @classmethod
    def _location_relevance_score(
        cls,
        requested_location: str,
        listing_location: str,
    ) -> int:
        """
        Calculate how strongly a listing location matches the
        requested location.

        Higher score means more meaningful location-term overlap.
        """

        requested_terms = cls._normalize_location(
            requested_location,
        )

        listing_terms = cls._normalize_location(
            listing_location,
        )

        if not requested_terms or not listing_terms:
            return 0

        return len(
            requested_terms.intersection(
                listing_terms,
            )
        )

    @classmethod
    def _location_matches(
        cls,
        requested_location: str,
        listing_location: str,
    ) -> bool:
        """
        Determine whether the listing has enough location overlap
        with the requested location.

        If no meaningful location terms can be extracted from the
        request, the search provider result is trusted and the
        listing is not rejected solely by this filter.
        """

        requested_terms = cls._normalize_location(
            requested_location,
        )

        if not requested_terms:
            return True

        score = cls._location_relevance_score(
            requested_location=requested_location,
            listing_location=listing_location,
        )

        return score > 0

    @classmethod
    def _filter_listings(
        cls,
        listings: list[ApartmentListing],
        location: str,
        budget: int | None,
        apartment_type: str | None,
        furnished: bool | None,
        parking: bool | None,
        brokerage: bool | None,
    ) -> list[ApartmentListing]:
        """
        Apply deterministic filters to extracted apartment listings.

        Only fields explicitly supported by the listing data are used
        for filtering.
        """

        filtered = []

        for listing in listings:

            # -------------------------------------------------
            # Budget
            # -------------------------------------------------

            if (
                budget is not None
                and listing.rent is not None
                and listing.rent > budget
            ):
                continue

            # -------------------------------------------------
            # Apartment type
            # -------------------------------------------------

            if (
                apartment_type
                and listing.apartment_type
                and listing.apartment_type.lower().strip()
                != apartment_type.lower().strip()
            ):
                continue

            # -------------------------------------------------
            # Location
            # -------------------------------------------------

            if not cls._location_matches(
                requested_location=location,
                listing_location=listing.location,
            ):
                continue

            # -------------------------------------------------
            # Furnished
            # -------------------------------------------------

            if furnished is True:
                if (
                    listing.furnished is not None
                    and "furnished"
                    not in listing.furnished.lower()
                ):
                    continue

            elif furnished is False:
                if (
                    listing.furnished is not None
                    and "unfurnished"
                    not in listing.furnished.lower()
                ):
                    continue

            # -------------------------------------------------
            # Parking
            # -------------------------------------------------

            if (
                parking is True
                and listing.parking is False
            ):
                continue

            elif (
                parking is False
                and listing.parking is True
            ):
                continue

            # -------------------------------------------------
            # Brokerage
            # -------------------------------------------------

            if (
                brokerage is False
                and listing.brokerage is True
            ):
                continue

            elif (
                brokerage is True
                and listing.brokerage is False
            ):
                continue

            filtered.append(listing)

        return filtered

    @classmethod
    def _rank_listings(
        cls,
        listings: list[ApartmentListing],
        requested_location: str,
    ) -> list[ApartmentListing]:
        """
        Rank listings by location relevance.

        Listings with more meaningful location-term overlap are
        placed first.
        """

        return sorted(
            listings,
            key=lambda listing: cls._location_relevance_score(
                requested_location=requested_location,
                listing_location=listing.location,
            ),
            reverse=True,
        )

    @staticmethod
    def _format_results(
        response: SearchResponse,
    ) -> str:
        """
        Convert Tavily apartment search results into the text
        consumed by the apartment extraction chain.
        """

        if not response.results:
            return "No apartments were found."

        formatted = []

        for index, result in enumerate(
            response.results,
            start=1,
        ):
            formatted.append(
                f"""
Result {index}

Title:
{result.title}

URL:
{result.url}

Content:
{result.content}
"""
            )

        return "\n".join(formatted)