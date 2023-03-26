# Object Oriented Programming Notes

# Things to look into:
# 1. Self
# 2. -> None and ->

# Mold is a class
# Object comes out of the mold
# Classes have instance variables and related methods that define a particular object type
# An instance of a class with defined properties is an object

# OOP allows you to code faster, and reuse code, while being legible

# Python has a constructor __new__ that is called when a new object is created
# __new__ is called before __init__
# __init__ is called when the object is initialized
# __new__ is to control the creation of a new instance
# while __init__ is used when you need to control the initialization of a new instance

# example Circle class
from math import pi
class Circle:

    # Constructor for the class with a radius and color property
    def __init__(self, radius: float, color: str = "blue") -> Self:
        self.radius = radius
        self.color = color

    def color(self) -> str:
        return self.color

    def circumference(self) -> float:
        # Returns a float of the circumference of the circle
        return self.radius * 2 * pi

    def area(self) -> float:
        # Returns a float of the area of the circle
        return self.radius ** 2 * pi

a = Circle(1)
b = Circle(2)
c = circle(3)

print(f"Area: {a.area()}")
print(a)