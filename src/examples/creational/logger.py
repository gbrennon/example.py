from typing import Optional

# Singleton example class that logs messages
class Logger:
    __instance: Optional['Logger'] = None

    def __new__(cls) -> 'Logger':
        if cls.__instance is None:
            cls.__instance = super(Logger, cls).__new__(cls)
        return cls.__instance

    def log(self, message: str) -> None:
        print(message)
