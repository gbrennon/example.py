# exmples.py

This project demonstrates the implementation of several common design patterns in Python, focusing on practical examples.
The goal is to help new learners understand the core concepts of design patterns, starting with the Singleton pattern.

## Project structure

This project is structured as follows:

```plaintext
    src
    ├── design_patterns
    │   ├── behavioral
    │   │   ├── __init__.py
    │   │   └── strategy.py
    │   ├── creational
    │   │   ├── factory_method.py
    │   │   ├── factory.py
    │   │   ├── __init__.py
    │   │   └── singleton.py
    │   ├── __init__.py
    │   └── structural
    │       ├── adapter.py
    │       └── __init__.py
    ├── examples
    │   ├── flask
    │   │   ├── adapters
    │   │   │   ├── __init__.py
    │   │   │   ├── weather_adapter.py
    │   │   │   └── weather_api_client_adapter.py
    │   │   ├── app.py
    │   │   ├── __init__.py
    │   │   ├── logger.py
    │   │   ├── services
    │   │   │   ├── discount_service.py
    │   │   │   ├── __init__.py
    │   │   │   └── weather_service.py
    │   │   ├── strategies
    │   │   │   ├── discount
    │   │   │   └── __init__.py
    │   │   ├── user_factory.py
    │   │   └── user.py
    │   └── __init__.py
    └── __init__.py
    tests
    ├── design_patterns
    │   ├── behavioral
    │   │   ├── __init__.py
    │   │   └── test_strategy.py
    │   ├── creational
    │   │   ├── __init__.py
    │   │   ├── test_factory_method.py
    │   │   ├── test_factory.py
    │   │   └── test_singleton.py
    │   ├── __init__.py
    │   └── structural
    │       ├── __init__.py
    │       └── test_adapter.py
    ├── examples
    │   ├── flask
    │   │   ├── adapters
    │   │   │   ├── __init__.py
    │   │   │   └── test_weather_api_client_adapter.py
    │   │   ├── strategy
    │   │   │   ├── discount
    │   │   │   └── __init__.py
    │   │   ├── test_logger.py
    │   │   ├── test_user_factory.py
    │   │   └── test_user.py
    │   └── __init__.py
    └── __init__.py
```

### Explanation of files and directories

- **src**: Contains the source code of the project.
  - **examples**: Contains examples of design patterns in practical applications.
    - **flask**: Contains an example of a Flask application.
  - **design_patterns**: Contains the implementation of various design patterns.
    - **creational**: Contains the implementation of creational design patterns.
    - **behavioral**: Contains the implementation of behavioral design patterns.
    - **structural**: Contains the implementation of structural design patterns.


## Installation

### Requirements

- Python 3.12 (or higher)
- Poetry (for managing dependencies)

### Steps

1. Clone the repository

```
git clone https://github.com/gbrennon/example.py.git
```

2. Navigate to the project directory

```
cd <project-directory>
```

3. Install the dependencies

```
poetry install
```

## Usage

1. Activate the virtual environment

```
poetry shell
```

2. Run tests

```
pytest
```

3. Run the application

```
poetry run python -m src.examples.flask.app
```

4. Open the browser and navigate to `http://localhost:5000`

## Conclusion

This project provides a practical demonstration of design patterns in Python,
focusing on the Singleton pattern. It aims to help new learners understand the
core concepts of design patterns and how they can be applied in real-world
scenarios.
