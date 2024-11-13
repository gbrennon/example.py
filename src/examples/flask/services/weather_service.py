from src.examples.flask.adapters.weather_api_client_adapter import (
    WeatherAPIClientAdapter
)
from src.examples.flask.adapters.weather_adapter import WeatherAdapter

class WeatherService:
    __weather_adapter: WeatherAdapter

    def __init__(self, weather_adapter: WeatherAdapter) -> None:
        self.__weather_adapter = weather_adapter

    def fetch_weather(self, city: str) -> dict[str, str]:
        return self.__weather_adapter.fetch_weather(city)

def create_weather_service(api_key: str) -> WeatherService:
    weather_adapter = WeatherAPIClientAdapter(api_key)

    return WeatherService(weather_adapter)
