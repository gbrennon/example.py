from flask import Flask

from src.examples.flask.logger import Logger
from src.examples.flask.services.weather_service import (
    create_weather_service,
)

app = Flask(__name__)
logger = Logger()
weather_api_key = "39bbc8668c644972816224326241211"
weather_service = create_weather_service(weather_api_key)

@app.route('/')
def hello_world():
    text = 'Hello, World!'
    logger.log(text)

    return text

@app.route('/weather/<city>')
def weather(city: str):
    logger.log(f"Fetching weather for {city}")
    weather = weather_service.fetch_weather(city)

    return weather


if __name__ == '__main__':
    app.run()
