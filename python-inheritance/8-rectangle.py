#!/usr/bin/python3
"""
This module defines a class `BaseGeometry` and a subclass `Rectangle`.
"""


class BaseGeometry:
    """A class for geometry operations."""

    def area(self):
        """Raises an exception indicating that the area method \
                is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is a positive integer.

        Args:
            name (str): The name of the value.
            value (int): The value to be validated.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    """A class representing a rectangle."""

    def __init__(self, width, height):
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"

if __name__ == "__main__":
    r = Rectangle(3, 5)
    print(r)
    print(f"Area: {r.area()}")
