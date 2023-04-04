#!/usr/bin/python3
# 1-square.py
"""Define a square class"""


class Square:
    """Represents a square"""

    def __init__(self, size):
        """Initialize a square

        Args:
            size(int): length of side of new square
        """
        self.__size = size
