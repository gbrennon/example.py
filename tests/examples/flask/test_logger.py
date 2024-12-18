import pytest

from _pytest.logging import LogCaptureFixture
from src.examples.flask.logger import Logger

class TestLogger:
    logger: Logger

    def setup_method(self):
        # This is the setup of the test
        self.logger = Logger()
        assert self.logger is not None

    def teardown_method(self):
        # This is the teardown of the test
        self.logger = None # type: ignore

    def test_logger_singleton_behaviour(self):
        # Arrange
        logger1 = Logger()
        logger2 = Logger()

        # Act
        result = logger1 is logger2

        # Assert
        assert result is True, "Logger instances are not the same"

    def test_log_success(self, caplog: LogCaptureFixture):
        # Arrange
        test_message = "Test message"

        # Act
        self.logger.log(test_message)

        # Assert
        assert test_message in caplog.text

    def test_log_without_initialization(self):
        # Arrange
        self.logger._logger = None

        # Act and Assert
        with pytest.raises(ValueError):
            self.logger.log("Test message")
