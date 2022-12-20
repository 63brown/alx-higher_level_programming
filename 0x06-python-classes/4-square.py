#!/usr/bin/python3
"""A class Square that defines a square"""


class Square:
    """Module of a square
    Attributes:
        __size (int): Describes the length of a square
    """
    def __init__(self, size=0):
        """Initializes the square attributes
        Args:
            size (int): Describes the length of a square
        Returns:
            None
        """
        self.size = size

    def area(self):
        """Calculates area of a square
        Returns:
            the current square area
        """
        return (f"{self.__size*self.__size}")

    @property
    def size(self):
        """getting the size
        Returns:
            the length of a square
        """
        return(self.__size)

    @size.setter
    def size(self, value):
        """setting the size
        Args:
            value (int): Describes the length of a square
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
