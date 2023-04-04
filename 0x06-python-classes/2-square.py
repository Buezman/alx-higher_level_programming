#!/usr/bin/python3
# 2-square.py
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
