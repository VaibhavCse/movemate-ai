class MoveMateError(Exception):
    """
    Base exception for MoveMate AI application errors.
    """

    def __init__(
        self,
        message: str,
        user_message: str | None = None,
    ):
        super().__init__(message)
        self.user_message = user_message or message


class SearchProviderError(MoveMateError):
    """
    Raised when a search provider fails.
    """