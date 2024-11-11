from unittest.mock import patch, MagicMock
from src.design_patterns.creational.factory_method import Entity
from typing import Generator
import pytest

# Generator[Unkown, Any, None]
@pytest.fixture
def mock_uuid4() -> Generator[MagicMock, None, None]:
    with patch(
        "src.design_patterns.creational.factory_method.uuid4"
    ) as mock_uuid4:
        yield mock_uuid4

class TestEntity:
    def test_create_returns_entity(self, mock_uuid4: MagicMock):
        # Arrange: Create a name for the entity
        name = "Test Entity"

        generated_id = "123e4567-e89b-12d3-a456-426614174000"
        mock_uuid4.return_value = generated_id
        
        # Act: The action is to create an entity
        entity = Entity.create(name)
        
        # Assert: The entity has the expected name
        assert entity.name == name, "The entity should have the expected name"

        assert (
            entity.id == generated_id
        ), "The entity should have the expected id"
