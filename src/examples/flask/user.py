class User:
    _id: str
    _email: str
    _name: str
    _password: str

    def __init__(self, id: str, name: str, email: str, password: str) -> None:
        self._id = id
        self._name = name
        self._email = email
        self._password = password

    @property
    def id(self) -> str:
        return self._id

    @property
    def email(self) -> str:
        return self._email

    @property
    def name(self) -> str:
        return self._name

    @property
    def password(self) -> str:
        return self._password
