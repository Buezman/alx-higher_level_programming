#!/usr/bin/python3
# 6-square.py
"""Define a square class"""


class Square:
    """Represents a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square

        Args:
            size(int): length of side of new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        err = "position must be a tuple of 2 positive integers"
        if not isinstance(position, tuple):
            raise TypeError(err)
        if len(position) != 2:
            raise TypeError(err)
        if not all(isinstance(num, int) for num in position):
            raise TypeError(err)
        if not all(num >= 0 for num in position):
            raise TypeError(err)
        self.__size = size
        self.__position = position

    def area(self):
        """Returns area of square"""
        return self.__size * self.__size

    @property
    def size(self):
        """Get the size of square"""
        return self.__size

    @size.setter
    def size(self, val):
        """updates the size of the square"""
        if not isinstance(val, int):
            raise TypeError("size must be an integer")
        if val < 0:
            raise ValueError("size must be >= 0")
        self.__size = val

    @property
    def position(self):
        """Gets the position of the square"""
        return self.__position

    @position.setter
    def position(self, val):
        """updates the position of the square"""
        err = "position must be a tuple of 2 positive integers"
        if not isinstance(val, tuple):
            raise TypeError(err)
        if len(val) != 2:
            raise TypeError(err)
        if not all(isinstance(num, int) for num in val):
            raise TypeError(err)
        if not all(num >= 0 for num in val):
            raise TypeError(err)
        self.__position = val

    def my_print(self):
        """prints a square"""
        if self.__size == 0:
            print("")
            return

        [print("") for x in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for n in range(0, self.__position[0])]
            [print("#", end="") for j in range(0, self.__size)]
            print("")
