from flask import Flask

from src.examples.flask.logger import Logger

app = Flask(__name__)
logger = Logger()

@app.route('/')
def hello_world():
    text = 'Hello, World!'
    logger.log(text)

    return text

if __name__ == '__main__':
    app.run()
