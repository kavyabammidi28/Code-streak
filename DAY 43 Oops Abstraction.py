from abc import ABC, abstractmethod

# Abstract base class
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass


# Derived class 1
class Car(Vehicle):
    def start_engine(self):
        print("Car engine started 🚗")

    def stop_engine(self):
        print("Car engine stopped ❌")


# Derived class 2
class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started 🏍️")

    def stop_engine(self):
        print("Bike engine stopped ❌")


# Example usage
vehicles = [Car(), Bike()]

for v in vehicles:
    v.start_engine()
    v.stop_engine()
