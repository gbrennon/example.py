from uuid import uuid4

from src.examples.flask.user import User

class UserFactory:
    @staticmethod
    def create(name: str, email: str, password: str) -> User:
        id = str(uuid4())

        return User(id, name, email, password)
