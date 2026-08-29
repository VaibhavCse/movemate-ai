from pydantic import BaseModel


class ApartmentListing(BaseModel):
    title: str
    location: str

    apartment_type: str | None = None

    rent: int | None = None
    maintenance: int | None = None
    deposit: int | None = None

    brokerage: bool | None = None

    furnished: str | None = None
    parking: bool | None = None

    area_sqft: int | None = None

    amenities: list[str] = []

    source: str | None = None
    url: str

class ApartmentExtractionResponse(BaseModel):
    listings: list[ApartmentListing]

class ApartmentSearchResponse(BaseModel):
    summary: str
    total_results: int
    listings: list[ApartmentListing]