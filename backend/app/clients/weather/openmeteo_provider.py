from typing import Any

import httpx

from app.core.config import settings
from app.core.exceptions import SearchProviderError


class OpenMeteoProvider:
    """
    Open-Meteo Weather Provider.

    Responsible for communicating with the Open-Meteo
    Geocoding and Weather Forecast APIs.
    """

    GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
    FORECAST_URL = "https://api.open-meteo.com/v1/forecast"

    async def get_weather(
        self,
        location: str,
    ) -> dict[str, Any]:

        timeout = httpx.Timeout(settings.REQUEST_TIMEOUT)

        try:
            async with httpx.AsyncClient(timeout=timeout) as client:

                # ---------------------------------------------------------
                # 1. Resolve location to coordinates
                # ---------------------------------------------------------

                geocoding_response = await client.get(
                    self.GEOCODING_URL,
                    params={
                        "name": location,
                        "count": 1,
                        "language": "en",
                        "format": "json",
                    },
                )

                geocoding_response.raise_for_status()

                geocoding_data = geocoding_response.json()

                results = geocoding_data.get("results", [])

                if not results:
                    raise SearchProviderError(
                        f"Unable to find weather location: {location}"
                    )

                place = results[0]

                latitude = place["latitude"]
                longitude = place["longitude"]

                resolved_location = place.get(
                    "name",
                    location,
                )

                country = place.get(
                    "country",
                    "",
                )

                admin1 = place.get(
                    "admin1",
                    "",
                )

                # ---------------------------------------------------------
                # 2. Get weather forecast
                # ---------------------------------------------------------

                forecast_response = await client.get(
                    self.FORECAST_URL,
                    params={
                        "latitude": latitude,
                        "longitude": longitude,
                        "current": (
                            "temperature_2m,"
                            "relative_humidity_2m,"
                            "apparent_temperature,"
                            "precipitation,"
                            "weather_code,"
                            "wind_speed_10m"
                        ),
                        "daily": (
                            "weather_code,"
                            "temperature_2m_max,"
                            "temperature_2m_min,"
                            "precipitation_probability_max,"
                            "sunrise,"
                            "sunset"
                        ),
                        "timezone": "auto",
                        "forecast_days": 3,
                    },
                )

                forecast_response.raise_for_status()

                forecast_data = forecast_response.json()

        except SearchProviderError:
            raise

        except httpx.HTTPStatusError as exc:
            raise SearchProviderError(
                f"Open-Meteo API returned {exc.response.status_code}"
            ) from exc

        except httpx.RequestError as exc:
            raise SearchProviderError(
                "Unable to connect to Open-Meteo."
            ) from exc

        return {
            "location": resolved_location,
            "admin1": admin1,
            "country": country,
            "latitude": latitude,
            "longitude": longitude,
            "timezone": forecast_data.get("timezone"),
            "current": forecast_data.get("current", {}),
            "current_units": forecast_data.get(
                "current_units",
                {},
            ),
            "daily": forecast_data.get("daily", {}),
            "daily_units": forecast_data.get(
                "daily_units",
                {},
            ),
        }