import pytest
from src.examples.flask.logger import Logger

class TestLogger:
    def test_logger_singleton_behaviour(self):
        # Arrange
        logger1 = Logger()
        logger2 = Logger()

        # Act
        result = logger1 is logger2

        # Assert
        assert result is True, "Logger instances are not the same"

    def test_log(self, caplog):
        # Arrange
        logger = Logger()

        # Act
        test_message = "Test message"
        logger.log(test_message)

        # Assert
        assert test_message in caplog.text
