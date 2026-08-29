import re

from langchain_core.messages import HumanMessage

from app.ai.state import ChatState
from app.schemas.preferences import UserPreferences


def update_preferences(
    current: UserPreferences,
    message: str,
) -> UserPreferences:
    """
    Update user preferences from the latest user message.

    Only explicitly identifiable preferences are updated.
    Existing preferences are preserved.
    """

    updated = current.model_copy()

    message_lower = message.lower()

    # Apartment type
    apartment_match = re.search(
        r"\b([1-4])\s*bhk\b",
        message_lower,
    )

    if apartment_match:
        updated.apartment_type = (
            f"{apartment_match.group(1)} BHK"
        )

    # Furnishing
    if any(
        phrase in message_lower
        for phrase in (
            "unfurnished",
            "non furnished",
            "not furnished",
        )
    ):
        updated.furnished = False

    elif "furnished" in message_lower:
        updated.furnished = True

    # Parking
    if any(
        phrase in message_lower
        for phrase in (
            "no parking",
            "without parking",
            "don't need parking",
            "do not need parking",
        )
    ):
        updated.parking = False

    elif "parking" in message_lower:
        updated.parking = True

    # Brokerage
    if any(
        phrase in message_lower
        for phrase in (
            "no broker",
            "without broker",
            "no brokerage",
            "without brokerage",
            "owner only",
            "direct owner",
        )
    ):
        updated.brokerage = False

    elif any(
        phrase in message_lower
        for phrase in (
            "broker is okay",
            "brokerage is okay",
            "with broker",
        )
    ):
        updated.brokerage = True

    # Maximum budget
    budget_match = re.search(
        r"(?:under|below|upto|up to|max(?:imum)?|"
        r"budget(?: of)?|within)\s*₹?\s*([\d,]+)",
        message_lower,
    )

    if budget_match:
        updated.budget_max = int(
            budget_match.group(1).replace(",", "")
        )

    # Minimum budget
    min_budget_match = re.search(
        r"(?:above|over|minimum|min)\s*₹?\s*([\d,]+)",
        message_lower,
    )

    if min_budget_match:
        updated.budget_min = int(
            min_budget_match.group(1).replace(",", "")
        )

    return updated


async def preference_node(
    state: ChatState,
):
    """
    Extract and update structured preferences
    from the latest user message.
    """

    current_preferences = (
        state.get("preferences")
        or UserPreferences()
    )

    messages = state.get("messages", [])

    # Find the latest actual user message.
    latest_user_message = None

    for message in reversed(messages):
        if isinstance(message, HumanMessage):
            latest_user_message = message
            break

    if latest_user_message is None:
        return {
            "preferences": current_preferences,
        }

    updated_preferences = update_preferences(
        current=current_preferences,
        message=latest_user_message.content,
    )

    return {
        "preferences": updated_preferences,
    }