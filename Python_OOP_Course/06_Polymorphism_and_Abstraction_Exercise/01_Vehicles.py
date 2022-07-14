from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    increased_consumption_to_add = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance):
        needed_fuel = distance * (self.fuel_consumption + __class__.increased_consumption_to_add)
        if self.fuel_quantity < needed_fuel:
            return

        self.fuel_quantity -= needed_fuel

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    increased_consumption_to_add = 1.6
    fuel_lost_from_hole_proportion = 0.05

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance):
        needed_fuel = distance * (self.fuel_consumption + __class__.increased_consumption_to_add)
        if self.fuel_quantity < needed_fuel:
            return

        self.fuel_quantity -= needed_fuel

    def refuel(self, fuel):
        self.fuel_quantity += fuel * (1 - __class__.fuel_lost_from_hole_proportion)
