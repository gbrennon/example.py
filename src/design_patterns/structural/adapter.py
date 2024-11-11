from abc import ABC, abstractmethod

class Adapter(ABC):
    @abstractmethod
    def adapt(self) -> str:
        pass

class Adaptee(ABC):
    @abstractmethod
    def specific_request(self) -> str:
        pass

class FooAdaptee:
    def specific_request(self) -> str:
        return "Foo Specific request"

class BarAdaptee:
    def specific_request(self) -> str:
        return "Bar Specific request"

class FooAdapter(Adapter):
    __adaptee: FooAdaptee

    def __init__(self, adaptee: FooAdaptee):
        self.__adaptee = adaptee

    def adapt(self) -> str:
        return self.__adaptee.specific_request()

class BarAdapter(Adapter):
    __adaptee: BarAdaptee

    def __init__(self, adaptee: BarAdaptee):
        self.__adaptee = adaptee

    def adapt(self) -> str:
        return self.__adaptee.specific_request()
