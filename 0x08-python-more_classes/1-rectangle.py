#!/usr/bin/python3
# 1-rectangle.py
"""Defines a Rectangle class"""


class Rectangle:
    """Describes a rectangle object"""
    
    def __init__(self, width, heigth):
        """Initialize a new Rectangle

        Args:
            width (int): Width of new Rectangle
            heigth (int): Height of new Rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, val):
        """sets the width"""
        if not isinstance(val, int):
            raise TypeError("width must be an integer")
        elif val < 0:
            raise ValueError("width must be >= 0")
        self.__width = val

    @property
    def heigth(self):
        """Getter for heigth"""
        return self.__heigth

    @heigth.setter
    def heigth(self, val):
        """sets the height"""
        if not isinstance(val, int):
            raise TypeError("heigth must be an integer")
        elif val < 0:
            raise ValueError("heigth must be >= 0")
        self.__height = val
