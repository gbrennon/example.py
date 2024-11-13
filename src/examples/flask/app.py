import os
from flask import Flask
from dotenv import load_dotenv

from src.examples.flask.logger import Logger
from src.examples.flask.services.weather_service import (
    create_weather_service,
)

load_dotenv()

def create_app():
    app = Flask(__name__)
    logger = Logger()
    weather_api_key = os.getenv("WEATHER_API_KEY")

    if weather_api_key is None:
        raise Exception("WEATHER_API_KEY is not set")

    weather_service = create_weather_service(weather_api_key)

    @app.route('/')
    def hello_world(): # type: ignore
        text = 'Hello, World!'
        logger.log(text)

        return text

    @app.route('/weather/<city>')
    def weather(city: str): # type: ignore
        logger.log(f"Fetching weather for {city}")
        weather = weather_service.fetch_weather(city)

        return weather

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
