from src.examples.flask.strategies.discount.no_discount_strategy import (
    NoDiscountStrategy
)

class TestNoDiscountStrategy:
    def test_apply_discount(self):
        # Arrange
        strategy = NoDiscountStrategy()

        # Act
        price = 100
        result = strategy.apply_discount(price)
        
        # Assert
        expected_result = price
        assert result == expected_result, "No discount should be applied"
