#!/usr/bin/python3
"""A class MagicClass that defines a circle"""
import math


class MagicClass:
    """Module of a circle
    Attributes:
        __radius (int): Describes the radius of a circle
    """
    def __init__(self, radius=0):
        """Initializes the circle attributes
        Args:
            radius (int): Describes the radius of a circle
        Returns:
            None
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculates area of a circle
        Returns:
            the current circle area
        """
        return ((self.__radius ** 2) * math.pi)

    def circumference(self):
        """Calculates circumference of a circle
        Returns:
            the current circle circumference
        """
        return (2 * math.pi * self.__radius)
