from src.design_patterns.structural.adapter import (
        FooAdapter,
        FooAdaptee,
        BarAdapter,
        BarAdaptee
)

class TestFooAdapter:
    def test_adapt(self):
        # Arrange
        adapter = FooAdapter(FooAdaptee())

        # Act
        result = adapter.adapt()

        # Assert
        assert result == "Foo Specific request"

class TestBarAdapter:
    def test_adapt(self):
        # Arrange
        adapter = BarAdapter(BarAdaptee())

        # Act
        result = adapter.adapt()

        # Assert
        assert result == "Bar Specific request"
