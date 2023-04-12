#!/usr/bin/python3
# 10-square.py
"""Describes a Square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A Square class"""

    def __init__(self, size):
        """Initializes a square object.

        Args:
            size (int): Length of side of square
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """calculates the area of square"""
        return self.__size * self.__size
