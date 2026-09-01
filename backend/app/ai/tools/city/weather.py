from typing import Type

from pydantic import BaseModel, Field

from app.ai.tools.base import MoveMateTool
from app.clients.weather.openmeteo_provider import OpenMeteoProvider
from app.clients.weather_client import WeatherClient
from app.services.city.weather_service import WeatherService


class WeatherInput(BaseModel):
    location: str = Field(
        ...,
        description=(
            "City, locality, or area to get the weather for. "
            "Examples: Bangalore, HSR Layout Bangalore, "
            "Koramangala Bangalore."
        ),
    )


class WeatherTool(MoveMateTool):
    name: str = "weather"

    description: str = (
        "Get current weather and a short forecast for a city or locality. "
        "Use this tool whenever the user asks about current weather, "
        "temperature, rain, forecast, or weather conditions."
    )

    args_schema: Type[BaseModel] = WeatherInput

    def _run(
        self,
        *args,
        **kwargs,
    ):
        raise NotImplementedError(
            "WeatherTool only supports async execution."
        )

    async def _arun(
        self,
        location: str,
    ):

        weather_client = WeatherClient(
            provider=OpenMeteoProvider(),
        )

        weather_service = WeatherService(
            weather_client=weather_client,
        )

        weather = await weather_service.get_weather(
            location=location,
        )

        current = weather.get("current", {})
        current_units = weather.get(
            "current_units",
            {},
        )

        daily = weather.get("daily", {})
        daily_units = weather.get(
            "daily_units",
            {},
        )

        return self.success_response(
            data={
                "location": weather.get("location"),
                "admin1": weather.get("admin1"),
                "country": weather.get("country"),
                "timezone": weather.get("timezone"),
                "current": current,
                "current_units": current_units,
                "forecast": daily,
                "forecast_units": daily_units,
            },
            message="Weather retrieved successfully.",
        )


weather_tool = WeatherTool()