import re

from app.schemas.apartment import ApartmentListing
from app.schemas.search import SearchResponse


class PropertyExtractor:
    """
    Extract structured apartment information from search results.
    """

    RENT_PATTERN = re.compile(r"₹\s?([\d,]+)")
    SQFT_PATTERN = re.compile(r"(\d+)\s*(sq\.?\s*ft|sqft)", re.IGNORECASE)

    def extract(
        self,
        response: SearchResponse,
    ) -> list[ApartmentListing]:

        listings: list[ApartmentListing] = []

        for result in response.results:

            rent = None
            area = None

            rent_match = self.RENT_PATTERN.search(result.content)

            if rent_match:
                rent = int(
                    rent_match.group(1).replace(",", "")
                )

            sqft_match = self.SQFT_PATTERN.search(result.content)

            if sqft_match:
                area = int(sqft_match.group(1))

            listings.append(
                ApartmentListing(
                    title=result.title,
                    location="Unknown",
                    rent=rent,
                    area_sqft=area,
                    url=result.url,
                    source="Tavily",
                )
            )

        return listings