from abc import ABC, abstractmethod

AdapterResult = dict[str, str]

class Adapter(ABC):
    @abstractmethod
    def adapt(self) -> AdapterResult:
        pass

class FooAdapter(Adapter):
    def adapt(self) -> AdapterResult:
        return {"foo": "Foo Specific request"}
