from src.examples.flask.strategies.discount.discount_strategy import (
    DiscountStrategy
) 
from src.examples.flask.strategies.discount.no_discount_strategy import (
    NoDiscountStrategy
) 

class DiscountService:
    def __init__(self, discount_strategy: DiscountStrategy):
        self.discount_strategy = discount_strategy

    def apply_discount(self, price: float) -> float:
        return self.discount_strategy.apply_discount(price)

def create_discount_service() -> DiscountService:
    discount_strategy = NoDiscountStrategy()

    return DiscountService(discount_strategy)
