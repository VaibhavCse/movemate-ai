from pydantic import Field

from app.schemas.common import BaseSchema


class ChatRequest(BaseSchema):
    """
    Incoming chat request.
    """

    message: str = Field(
        ...,
        min_length=1,
        max_length=4000,
        description="User message.",
        examples=["Find me a 2BHK near Bellandur under ₹35,000"],
    )

    session_id: str | None = Field(
        default=None,
        description="Conversation session identifier.",
    )