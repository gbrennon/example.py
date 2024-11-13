import pytest
import requests_mock
from requests.exceptions import HTTPError

from src.examples.flask.adapters.weather_api_client_adapter import(
    WeatherAPIClientAdapter
)


class TestWeatherAPIClientAdapter:
    __fake_api_key = "fake-api-key"

    @pytest.fixture
    def weather_adapter(self):
        return WeatherAPIClientAdapter(api_key=self.__fake_api_key)

    def test_fetch_weather_success(
        self,
        requests_mock: requests_mock.Mocker,
        weather_adapter: WeatherAPIClientAdapter
    ):
        # Arrange
        api_key = self.__fake_api_key
        city = "Sao Paulo"
        # Accessing private attribute to mock the URL
        mock_url = weather_adapter._WeatherAPIClientAdapter__url # type: ignore
        # Mocking the response
        mock_data = {
            "location": {
                "country": "Brazil",
                "region": "SP"
            },
            "current": {
                "temp_c": 25.0
            }
        }
        # Mocking the request
        requests_mock.get(
            f"{mock_url}?key={api_key}&q={city}&aqi=no",
            json=mock_data
        )

        # Act
        result = weather_adapter.fetch_weather(city)

        # Assert
        expected_result = {
            "city": city,
            "country": "Brazil",
            "state": "SP",
            "temperature": 25.0
        }
        assert result == expected_result, "Result is different than expected"
