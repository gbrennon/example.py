from typing import Optional

DO_SOMETHING = "Singleton doing something"

class Singleton:
    _instance: Optional['Singleton'] = None
    _initialized: bool = False

    def __new__(cls, *args, **kwargs) -> 'Singleton':
        # Ensure only one instance of the class is created
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def __init__(self,) -> None:
        # Ensure the class is initialized only once
        if not self._initialized:
            self._initialized = True

    def do_something(self) -> str:
        # Do something
        return DO_SOMETHING
