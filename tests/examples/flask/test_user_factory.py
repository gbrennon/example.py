import pytest
from unittest.mock import patch, MagicMock
from typing import Generator

from src.examples.flask.user_factory import UserFactory

@pytest.fixture
def mock_uuid4() -> Generator[MagicMock, None, None]:
    with patch(
        "src.examples.flask.user_factory.uuid4"
    ) as mock_uuid4:
        yield mock_uuid4

class TestUserFactory:
    def test_create_returns_user(self, mock_uuid4: MagicMock):
        # Arrange: Create a name for the user
        name = "Test user"
        email = "test@email.com"
        password = "password"

        generated_id = "123e4567-e89b-12d3-a456-426614174000"
        mock_uuid4.return_value = generated_id

        # Act: The action is to create an user
        user = UserFactory.create(name, email, password)
        
        # Assert: The user has the expected attributes
        assert (
            user.id == generated_id
        ), "The user should have the expected id"
        assert user.name == name, "The user should have the expected name"
        assert user.email == email, "The user should have the expected email"
        assert(
            user.password == password
        ), "The user should have the expected password"
