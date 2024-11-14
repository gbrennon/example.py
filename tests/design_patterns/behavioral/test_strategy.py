from src.design_patterns.behavioral.strategy import (
    NoDiscountStrategy,
    PercentageDiscountStrategy,
    ShoppingCart
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

class TestPercentageDiscountStrategy:
    def test_apply_discount(self):
        # Arrange
        percentage = 10
        strategy = PercentageDiscountStrategy(percentage)

        # Act
        price = 100
        result = strategy.apply_discount(price)
        
        # Assert
        expected_result = 90
        assert (
            result == expected_result
        ), "Percentage discount should be applied"

class TestShoppingCart:
    def test_add_item(self):
        # Arrange
        discount_strategy = NoDiscountStrategy()
        shopping_cart = ShoppingCart(discount_strategy)

        # Act
        shopping_cart.add_item("item1", 100)
        shopping_cart.add_item("item2", 200)
        
        # Assert
        expected_items = [("item1", 100), ("item2", 200)]
        assert (
            shopping_cart.items == expected_items
        ), "Items were not added correctly"

    def test_calculate_total_with_no_discount(self):
        # Arrange
        discount_strategy = NoDiscountStrategy()
        shopping_cart = ShoppingCart(discount_strategy)
        shopping_cart.add_item("item1", 100)
        shopping_cart.add_item("item2", 200)

        # Act
        result = shopping_cart.calculate_total()
        
        # Assert
        expected_result = 300
        assert result == expected_result, "No discount should be applied"

    def test_calculate_total_with_percentage_discount(self):
        # Arrange
        percentage = 10
        discount_strategy = PercentageDiscountStrategy(percentage)
        shopping_cart = ShoppingCart(discount_strategy)
        shopping_cart.add_item("item1", 100)
        shopping_cart.add_item("item2", 200)

        # Act
        result = shopping_cart.calculate_total()
        
        # Assert
        expected_result = 270
        assert (
            result == expected_result
        ), "Percentage discount should be applied"
