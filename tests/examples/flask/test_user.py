import pytest

from src.examples.flask.user import User

class TestUser:
    def test_id(self):
        # Arrange: Create a user
        id = "123e"
        user = User(id, "Test User", "test@example.com", "password")

        # Act: The action is to get the user's id
        actual_id = user.id

        # Assert: The user's id is the expected value
        expected_id = id
        assert actual_id == expected_id, "The user's id should be the expected value"

    def test_email(self):
        # Arrange: Create a user
        email = "test@example.com"
        user = User("123e", "Test User", email, "password")

        # Act: The action is to get the user's email
        actual_email = user.email

        # Assert: The user's email is the expected value
        expected_email = email
        assert(
            actual_email == expected_email
        ), "The user's email should be the expected value"

    def test_name(self):
        # Arrange: Create a user
        name = "Test User"
        user = User("123e", name, "test@example.com", "password")

        # Act: The action is to get the user's name
        actual_name = user.name

        # Assert: The user's name is the expected value
        expected_name = name
        assert(
            actual_name == expected_name
        ), "The user's name should be the expected value"

    def test_password(self):
        # Arrange: Create a user
        password = "password"
        user = User("123e", "Test User", "test@example.com", password)

        # Act: The action is to get the user's password
        actual_password = user.password

        # Assert: The user's password is the expected value
        expected_password = password
        assert(
            actual_password == expected_password
        ), "The user's password should be the expected value"
