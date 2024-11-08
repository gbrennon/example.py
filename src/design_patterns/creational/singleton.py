from typing import Any, Optional

class Singleton:
    __instance: Optional['Singleton'] = None
    __value: Any
    __initialized: bool = False

    def __new__(
        cls,
        *args: tuple[Any, ...],
    ) -> 'Singleton':
        if cls.__instance is None:
            cls.__instance = super(Singleton, cls).__new__(cls)

            if args:
                cls.__value = args[0]
        return cls.__instance

    def __init__(self, value: Any) -> None:
        if not self.__initialized:
            self.__value = value
            self.__initialized = True


    @property
    def value(self) -> Any:
        return self.__value

    @value.setter
    def value(self, new_value: Any) -> None:
        self.__value = new_value
