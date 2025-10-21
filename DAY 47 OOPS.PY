# Day 50: Inheritance + Polymorphism (Final OOPs Wrap)
# Problem:
# Create a class hierarchy with Animal as a base class and Dog,
#  Cat as subclasses overriding the sound() method.

class Animal:
    def sound(self):
        raise NotImplementedError("Subclass must implement this method")

class Dog(Animal):
    def sound(self):
        return "Bark 🐶"

class Cat(Animal):
    def sound(self):
        return "Meow 🐱"

# Example usage
animals = [Dog(), Cat()]

for a in animals:
    print(f"{a.__class__.__name__} makes sound: {a.sound()}")
