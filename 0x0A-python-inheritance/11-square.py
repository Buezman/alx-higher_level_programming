#!/usr/bin/python3
# 11-square.py
"""Describes a Square class"""
Rectangle = __import__('9-Rectangle').Rectangle


class Square(Rectangle):
    """A Square class"""

    def __init__(self, size):
        """Initializes a square object.

        Args:
            size (int): Length of side of square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """calculates the area of square"""
        return self.__size * self.__size

    def __str__(self):
        """Returns the print() and str() representation of Square"""

        return super().__str__(self)
