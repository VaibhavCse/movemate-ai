from typing import Any

from app.clients.weather.openmeteo_provider import OpenMeteoProvider


class WeatherClient:
    """
    Client responsible for accessing weather data.
    """

    def __init__(
        self,
        provider: OpenMeteoProvider,
    ):
        self.provider = provider

    async def get_weather(
        self,
        location: str,
    ) -> dict[str, Any]:

        return await self.provider.get_weather(
            location=location,
        )