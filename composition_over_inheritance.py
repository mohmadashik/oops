# write an example for when to use composition over inheritance
# and when to use inheritance over composition
# Inheritance is used when there is a clear "is-a" relationship
# Composition is used when there is a clear "has-a" relationship
# Inheritance is used when you want to create a new class that is a specialized version of an existing class
# Composition is used when you want to create a new class that is made up of existing classes

# code examples
# Inheritance example
class Animal:
    def speak(self):
        return "Animal speaks"
class Dog(Animal):
    def speak(self):
        return "Dog barks"
class Cat(Animal):
    def speak(self):
        return "Cat meows"
# Composition example
class Engine:
    def start(self):
        return "Engine starts"
class Car:
    def __init__(self):
        self.engine = Engine()
    def start(self):
        return self.engine.start() + " and Car starts"
# Inheritance example
class Shape:
    def area(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side * self.side
# Composition example
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

# applications for inheritance and composition
# Inheritance is used when you want to create a new class that is a specialized version of an existing class
# Composition is used when you want to create a new class that is made up of existing classes
