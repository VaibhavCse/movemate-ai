from typing import Type

from pydantic import BaseModel, Field

from app.ai.tools.base import MoveMateTool
from app.core.exceptions import MoveMateError
from app.dependencies.housing import get_apartment_service


class ApartmentSearchInput(BaseModel):
    location: str = Field(
        ...,
        description="City or locality to search apartments in.",
    )

    budget: int | None = Field(
        default=None,
        description="Maximum monthly rent budget.",
    )

    apartment_type: str | None = Field(
        default=None,
        description="Apartment type like 1 BHK, 2 BHK, or 3 BHK.",
    )

    furnished: bool | None = Field(
        default=None,
        description="Whether the apartment should be furnished.",
    )

    parking: bool | None = Field(
        default=None,
        description="Whether parking is required.",
    )

    brokerage: bool | None = Field(
        default=None,
        description=(
            "Whether broker-based listings are acceptable. "
            "False means owner/no-broker only."
        ),
    )

    gym_required: bool = Field(
        default=False,
        description=(
            "Whether the user wants nearby gyms. "
            "Set to true when the user mentions a gym, Cult, "
            "fitness center, or similar requirement."
        ),
    )

    gym_type: str | None = Field(
        default=None,
        description=(
            "Type of gym requested by the user. "
            "Use 'cult' when the user mentions Cult or Cult.fit. "
            "Use 'general' when the user asks for a gym or fitness center "
            "without specifying Cult."
        ),
    )


class ApartmentSearchTool(MoveMateTool):
    name: str = "apartment_search"

    description: str = (
        "Search for rental apartments based on location, budget, "
        "apartment type, furnishing, parking, brokerage preferences, "
        "and nearby gym requirements."
    )

    args_schema: Type[BaseModel] = ApartmentSearchInput

    def _run(self, *args, **kwargs):
        raise NotImplementedError(
            "ApartmentSearchTool only supports async execution."
        )

    async def _arun(
        self,
        location: str,
        budget: int | None = None,
        apartment_type: str | None = None,
        furnished: bool | None = None,
        parking: bool | None = None,
        brokerage: bool | None = None,
        gym_required: bool = False,
        gym_type: str | None = None,
    ):
        try:
            apartment_service = get_apartment_service()

            response = await apartment_service.search_apartments(
                location=location,
                budget=budget,
                apartment_type=apartment_type,
                furnished=furnished,
                parking=parking,
                brokerage=brokerage,
                gym_required=gym_required,
                gym_type=gym_type
            )

            return self.success_response(
                data={
                    "location": location,
                    "summary": response.summary,
                    "total_results": response.total_results,
                    "listings": [
                        listing.model_dump()
                        for listing in response.listings
                    ],
                    "nearby_places": response.nearby_places,
                },
                message="Apartment search completed successfully.",
            )

        except MoveMateError:
            return self.error_response(
                message=(
                    "Apartment search is temporarily unavailable. "
                    "Please try again shortly."
                )
            )

        except Exception:
            return self.error_response(
                message=(
                    "Apartment search could not be completed right now. "
                    "Please try again shortly."
                )
            )


apartment_search_tool = ApartmentSearchTool()