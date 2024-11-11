from uuid import uuid4

class Entity:
    _id: str
    _name: str

    def __init__(self, id: str, name: str):
        self._id = id
        self._name = name

    @property
    def id(self) -> str:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @staticmethod
    def create(name: str) -> "Entity":
        id = str(uuid4())

        return Entity(id, name)
