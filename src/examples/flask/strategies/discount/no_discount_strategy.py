from src.examples.flask.strategies.discount.discount_strategy import (
    DiscountStrategy
)
class NoDiscountStrategy(DiscountStrategy):
    def apply_discount(self, price: float) -> float:
        return price
