#!/usr/bin/python3
# 5-square.py
"""Define a square class"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initialize a square

        Args:
            size(int): length of side of new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

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

    def my_print(self):
        """prints a square"""
        if self.__size == 0:
            return ""

        for i in range(self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
