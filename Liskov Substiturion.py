# Принцип подстановки Барбары Лисков: объекты в программе
# должны быть заменяемы экземплярами их подтипов без ущерба
# работы программы
from typing import (
    TypeAlias,
    Sequence,
    Dict,
    Tuple,
    NamedTuple
)


# Нарушение принципа подстановки

# class Car:
#     def __init__(self, type: str):
#         self.type = type


# class PetrolCar(Car):
#     def __init__(self, type: str):
#         self.type = type


# car = Car('SUV')
# car.properties: Dict = {'Color': 'Red',
#                         'Gear': 'Auto',
#                         'Capacity': 6}

# petrol_car = PetrolCar('Sedan')
# petrol_car.properties: Tuple = ('Blue', 'Manual', 4)

# cars: Sequence[Car] = [car, petrol_car]


# def find_red_cars(cars) -> None:
#     red_cars: int = 0
#     for car in cars:
#         if car.properties['Color'] == 'Red':
#             red_cars += 1
#     print(f'Number of Red Cars = {red_cars}')


# find_red_cars(cars)


# Корректная реализация с сеттерами и геттерами

ValueType: TypeAlias = str | int

class CarProperties(NamedTuple):
    color: str
    gear: str
    capacity: int
 

class Car:
    def __init__(self, type: str) -> None:
        self.type = type
        self.car_properties: CarProperties = {}

    def set_properties(self, color: ValueType, gear: ValueType,
                       capacity: ValueType) -> None:
        self.car_properties: CarProperties =\
            CarProperties(color=color, gear=gear, capacity=capacity)

    def get_properties(self) -> CarProperties:
        return self.car_properties


class PetrolCar(Car):
    pass

car = Car('SUV')
car.set_properties('Red', 'Auto', 6)

petrol_car = PetrolCar('Sedan')
petrol_car.set_properties('Blue', 'Manual', 4)

cars = [car, petrol_car]


def find_red_cars(cars: Sequence[Car]):
    red_cars: int = 0
    for car in cars:
        if car.get_properties().color == 'Red':
            red_cars += 1
    print(f'Number of Red Cars = {red_cars}')

find_red_cars(cars)