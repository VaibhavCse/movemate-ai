from enum import Enum


class MessageRole(str, Enum):
    """
    Supported conversation roles.
    """

    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"