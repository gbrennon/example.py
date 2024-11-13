import requests
from typing import Any

from src.examples.flask.adapters.weather_adapter import WeatherAdapter

class WeatherAPIClientAdapter(WeatherAdapter):
    __api_key: str
    __url: str = "https://api.weatherapi.com/v1/current.json"

    def __init__(self, api_key: str) -> None:
        self.__api_key = api_key

    def fetch_weather(self, city: str) -> dict[str, Any]:
        parameters = {
            "key": self.__api_key,
            "q": city,
            "aqi": "no" # Disable air quality index to simplify the response
        }
        response = requests.get(self.__url, params=parameters)

        if response.status_code != 200:
            exception_content = (
                f"Failed to fetch weather data for {city}: "
                f"{response.status_code} - {response.text}"
            )
            raise Exception(exception_content)

        data = response.json()

        return {
            "city": city,
            "country": data['location']['country'],
            "state": data['location']['region'],
            "temperature": data['current']['temp_c']
        }
