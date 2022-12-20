#!/usr/bin/python3
"""A class Square that defines a square"""


class Square:
    """Module of a square
    Attributes:
        __size (int): Describes the length of a square
        __position (tuple): Shows the x and y positions
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square attributes
        Args:
            size (int): Describes the length of a square
            position (tuple): Shows the x and y positions
        Returns:
            None
        """
        self.size = size
        self.position = position

    def area(self):
        """Calculates area of a square
        Returns:
            the current square area
        """
        return (f"{self.__size*self.__size}")

    def my_print(self):
        """Prints in stdout the square with the character #
        Returns:
            None
        """
        if self.__size == 0:
            print()
        for i in range(self.__position[1]):
            print()
        for j in range(self.__size):
            print("".join([" " for m in range(self.__position[0])]), end="")
            print("".join(["#" for n in range(self.__size)]))

    @property
    def size(self):
        """getting the size
        Returns:
            the length of a square
        """
        return(self.__size)

    @property
    def position(self):
        """getting the position
        Returns:
            the x and y positions
        """
        return(self.__position)

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

    @position.setter
    def position(self, value):
        """setting the size
        Args:
            value (int): Shows the x and y positions
        Returns:
            None
        """
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def __str__(self):
        """Represents the Square objects as a string
        Returns:
            the representing string
        """
        if self.size == 0:
            return ("")
        string = "\n" * self.position[1] + (" " * self.position[0] +
                                            "#" * self.size + "\n") * self.size
        return (string[:-1])
