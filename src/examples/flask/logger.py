import sys
import logging
from typing import Optional

class Logger:
    _instance: Optional['Logger'] = None
    _logger: Optional[logging.Logger] = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._initialize_logger(cls._instance)
        return cls._instance

    @staticmethod
    def _initialize_logger(instance: "Logger"):
        instance._logger = logging.getLogger(__name__)
        instance._logger.setLevel(logging.INFO)

        # Ensure the handler writes to stdout
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        instance._logger.addHandler(handler)

    def log(self, message: str):
        if not self._logger:
            raise ValueError("Logger is not initialized")
        self._logger.info(message)
