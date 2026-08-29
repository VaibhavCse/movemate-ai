from pydantic import Field

from app.schemas.common import BaseSchema


class ChatResponse(BaseSchema):
    """
    Chat response returned to the client.
    """

    reply: str = Field(
        ...,
        description="Assistant reply.",
    )

    session_id: str | None = Field(
        default=None,
        description="Conversation session identifier.",
    )