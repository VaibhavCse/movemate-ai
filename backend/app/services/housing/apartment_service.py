from app.ai.chains.apartment_extraction import ApartmentExtractionChain
from app.schemas.apartment import ApartmentListing, ApartmentSearchResponse
from app.schemas.search import SearchResponse
from app.services.llm.summarizer_service import SummarizerService
from app.services.search.search_service import SearchService


class ApartmentService:
    """
    Service responsible for apartment-related search operations.
    """

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
    ) -> ApartmentSearchResponse:

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

        summary = await self.summarizer.summarize(
            title=f"Apartments in {location}",
            content=self._format_listings_for_summary(listings),
        )

        return ApartmentSearchResponse(
            summary=summary,
            total_results=len(listings),
            listings=listings,
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

    @staticmethod
    def _filter_listings(
        listings: list[ApartmentListing],
        location: str,
        budget: int | None,
        apartment_type: str | None,
        furnished: bool | None,
        parking: bool | None,
        brokerage: bool | None,
    ) -> list[ApartmentListing]:

        filtered = []

        requested_location = location.lower().strip()

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

            listing_location = listing.location.lower()

            # Only remove a listing when its location is
            # explicitly known to be unrelated.
            if (
                requested_location
                and requested_location not in listing_location
            ):
                # Keep the listing if the location is broad
                # and appears to be a related HSR area.
                related_locations = (
                    "hsr",
                    "hsr layout",
                )

                if (
                    "hsr" not in requested_location
                    or not any(
                        value in listing_location
                        for value in related_locations
                    )
                ):
                    continue

            # -------------------------------------------------
            # Furnished
            # -------------------------------------------------

            if furnished is True:
                if (
                    listing.furnished is not None
                    and "furnished" not in listing.furnished.lower()
                ):
                    continue

            elif furnished is False:
                if (
                    listing.furnished is not None
                    and "unfurnished" not in listing.furnished.lower()
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

    @staticmethod
    def _format_results(
        response: SearchResponse,
    ) -> str:

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

    @staticmethod
    def _format_listings_for_summary(
        listings: list[ApartmentListing],
    ) -> str:

        if not listings:
            return "No listings matched the requested criteria."

        formatted = []

        for index, listing in enumerate(
            listings,
            start=1,
        ):
            formatted.append(
                f"""
Listing {index}

Title:
{listing.title}

Location:
{listing.location}

Apartment Type:
{listing.apartment_type}

Rent:
{listing.rent}

Maintenance:
{listing.maintenance}

Brokerage:
{listing.brokerage}

Furnished:
{listing.furnished}

Parking:
{listing.parking}

Area:
{listing.area_sqft}

Amenities:
{", ".join(listing.amenities)}

Source:
{listing.source}

URL:
{listing.url}
"""
            )

        return "\n".join(formatted)