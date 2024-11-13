from abc import ABC, abstractmethod

class WeatherAdapter(ABC):
    @abstractmethod
    def fetch_weather(self, city: str) -> dict[str, str]:
        pass
