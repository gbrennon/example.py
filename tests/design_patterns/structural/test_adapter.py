from src.design_patterns.structural.adapter import (
        FooAdapter,
)

class TestFooAdapter:
    def test_adapt(self):
        # Arrange
        adapter = FooAdapter()

        # Act
        result = adapter.adapt()

        # Assert
        expected_result = {"foo": "Foo Specific request"}
        assert result == expected_result
