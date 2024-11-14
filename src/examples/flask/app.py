import os
from flask import Flask
from dotenv import load_dotenv

from src.examples.flask.logger import Logger
from src.examples.flask.services.weather_service import (
    create_weather_service,
)
from src.examples.flask.services.discount_service import (
    create_discount_service
)

load_dotenv()

def create_app():
    app = Flask(__name__)
    logger = Logger()
    weather_api_key = os.getenv("WEATHER_API_KEY")
    discount_service = create_discount_service()

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

    @app.route('/no_discount/<price>')
    def no_discount(price: float): # type: ignore
        logger.log(f"Applying no discount to price {price}")
        
        return {
            "price_after_discount": discount_service.apply_discount(price)
        }

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
