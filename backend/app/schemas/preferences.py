from pydantic import BaseModel, Field


class UserPreferences(BaseModel):
    """
    Structured preferences collected from the user's conversation.
    """

    city: str | None = Field(
        default=None,
        description="Preferred city.",
    )

    locality: str | None = Field(
        default=None,
        description="Preferred locality or neighborhood.",
    )

    budget_min: int | None = Field(
        default=None,
        description="Minimum monthly rent budget.",
    )

    budget_max: int | None = Field(
        default=None,
        description="Maximum monthly rent budget.",
    )

    apartment_type: str | None = Field(
        default=None,
        description="Preferred apartment type such as 1 BHK or 2 BHK.",
    )

    furnished: bool | None = Field(
        default=None,
        description="Whether the user prefers a furnished apartment.",
    )

    parking: bool | None = Field(
        default=None,
        description="Whether parking is required.",
    )

    brokerage: bool | None = Field(
        default=None,
        description="Whether the user is willing to consider brokered properties.",
    )

    commute_destination: str | None = Field(
        default=None,
        description="Office, workplace, or other commute destination.",
    )