from typing import Any

from app.clients.weather_client import WeatherClient


class WeatherService:
    """
    Service responsible for weather-related operations.
    """

    def __init__(
        self,
        weather_client: WeatherClient,
    ):
        self.weather_client = weather_client

    async def get_weather(
        self,
        location: str,
    ) -> dict[str, Any]:

        return await self.weather_client.get_weather(
            location=location,
        )