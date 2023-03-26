from abc import ABC, abstractmethod
from math import pi


# All classes must use a float method (?)
class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        # Returns: float: area of the shape
        pass


# Class for a circle defined by its radius
class Circle(Shape):
    # Constructor for a circle defined by its radius
    # Args: radius (float): radius of the circle
    # Returns: None
    # __ declares private characteristics (?)
    def __init__(self, radius: float) -> None:
        self.radius = radius

    # Calculate the circumference of the circle
    # Abstracts the circumference away from the user
    def circumference(self):
        return 2 * pi * self.radius

    # Calculate the area of the circle
    # Abstracts the area away from the user
    # Polymorphic: area() is defined in Shape
    def area(self) -> float:
        return pi * self.radius ** 2

    def __repr__(self) -> str:
        # __repr__ is supposed to be unambiguous... eg. for logging
        # If __str__ is not defined, __repr__ is used instead
        # Returns: str: description of the circle
        return f"Instance of {self.__class__} with radius {self.radius}"

    def __str__(self) -> str:
        # __str__ is supposed to be readable
        # Returns: str: description of the circle
        return f"A circle with a radius of {self.radius}, "       \
               f"a circumference of {self.circumference():.3f}, " \
               f"and an area of {self.area():.3f}"  # what is ():.3f?

    def __eq__(self, __o: object):  # what is __o?
        # Define equality for two circles
        # Args: __o (object): object to compare to
        # Returns: bool: True if other circle has same radius
        return isinstance(__o, self.__class__) and __o.radius == self.radius


# Class for a square defined by its radius (1/2 side)
class Square(Shape):
    # Constructor for a square defined by its radius
    # Args: radius (float): radius of the square
    # Returns: None
    # __ declares private characteristics (?)
    def __init__(self, radius: float) -> None:
        self.radius = radius

    # Calculate the area of the circle
    # Abstracts the area away from the user
    # Polymorphic: area() is defined in Shape
    def area(self) -> float:
        return self.radius * 4

    def __repr__(self) -> str:
        # __repr__ is supposed to be unambiguous... eg. for logging
        # If __str__ is not defined, __repr__ is used instead
        # Returns: str: description of the square
        return f"Instance of {self.__class__} with radius {self.radius}"

    def __str__(self) -> str:
        # __str__ is supposed to be readable
        # Returns: str: description of the square
        return f"A square with a radius of {self.radius}, " \
               f"and an area of {self.area():.3f}"  # what is ():.3f? Rounding?

    def __eq__(self, __o: object):  # what is __o?
        # Define equality for two circles
        # Args: __o (object): object to compare to
        # Returns: bool: True if other circle has same radius
        return isinstance(__o, self.__class__) and __o.radius == self.radius


# Tests
a = Circle(1)
b = Circle(2)
c = Circle(2)

shapes = [Circle(2), Square(3)]

print(a.__repr__())
print(a)
print(a == b)  # Not true, radii 1 != 2
print(b == c)  # Equality
print(b is c)  # Identity

for shape in shapes:
    print(f'{shape} has an area of {shape.area():.3f}')
