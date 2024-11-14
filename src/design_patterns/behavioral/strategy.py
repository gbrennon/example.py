from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, price: float) -> float:
        pass

class NoDiscountStrategy(DiscountStrategy):
    def apply_discount(self, price: float) -> float:
        return price

class PercentageDiscountStrategy(DiscountStrategy):
    def __init__(self, percentage: float):
        self.percentage = percentage

    def apply_discount(self, price: float) -> float:
        return price * (1 - self.percentage / 100)

class ShoppingCart:
    def __init__(self, discount_strategy: DiscountStrategy):
        self.discount_strategy = discount_strategy
        self.items: list[tuple[str, float]] = []

    def add_item(self, item_name: str, price: float):
        self.items.append((item_name, price))

    def calculate_total(self) -> float:
        total = sum(price for _, price in self.items)
        return self.discount_strategy.apply_discount(total)
