from src.design_patterns.creational.factory import EntityFactory
from unittest.mock import patch, MagicMock
from typing import Generator
import pytest

@pytest.fixture
def mock_uuid4() -> Generator[MagicMock, None, None]:
    with patch(
        "src.design_patterns.creational.factory.uuid4"
    ) as mock_uuid4:
        yield mock_uuid4

class TestEntityFactory:
    def test_create_returns_entity(self, mock_uuid4: MagicMock):
        # Arrange: Create a name for the entity
        name = "Test Entity"

        generated_id = "123e4567-e89b-12d3-a456-426614174000"
        mock_uuid4.return_value = generated_id

        # Act: The action is to create an entity
        entity = EntityFactory.create(name)
        
        # Assert: The entity has the expected name
        assert entity.name == name, "The entity should have the expected name"

        assert (
            entity.id == generated_id
        ), "The entity should have the expected id"
