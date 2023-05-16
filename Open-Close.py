# Принцип открытости/закрытости: сущности программы
# (классы, модули, функции и др.) должны быть открыты для
# расширения, но закрыты для изменений
from enum import Enum
from abc import abstractmethod


class Products(Enum):
    SHIRT = 1
    TSHIRT = 2
    PANT = 3


# Некорректная версия

# class DiscountCalculator:
#     def __init__(self, product_type: Products,
#                  cost: float) -> None:
#         self.product_type = product_type
#         self.cost = cost

#     def get_discounted_price(self) -> float:
#         if self.product_type == Products.SHIRT:
#             return self.cost - (self.cost * 0.10)
#         elif self.product_type == Products.TSHIRT:
#             return self.cost - (self.cost * 0.15)
#         elif self.product_type == Products.PANT:
#             return self.cost - (self.cost * 0.25)


# Реализация согласно принципу открытости/закрытости

class DiscountCalculator:
    @abstractmethod
    def get_discounted_price(self):
        pass


class DiscountCalculatorShirt(DiscountCalculator):
    def __init__(self, cost: float) -> None:
        self.cost = cost

    def get_discounted_price(self) -> float:
        return self.cost - (self.cost * 0.10)
    

class DiscountCalculatorTshirt(DiscountCalculator):
    def __init__(self, cost: float) -> None:
        self.cost = cost

    def get_discounted_price(self) -> float:
        return self.cost - (self.cost * 0.15)


class DiscountCalculatorPant(DiscountCalculator):
    def __init__(self, cost: float) -> None:
        self.cost = cost

    def get_discounted_price(self) -> float:
        return self.cost - (self.cost * 0.25)
