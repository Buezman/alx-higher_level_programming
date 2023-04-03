#!/usr/bin/python3
# 4-rectangle.py
"""Defines a Rectangle class"""


class Rectangle:
    """Describes a rectangle object"""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle

        Args:
            width (int): Width of new Rectangle
            height (int): Height of new Rectangle
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
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, val):
        """sets the height"""
        if not isinstance(val, int):
            raise TypeError("height must be an integer")
        elif val < 0:
            raise ValueError("height must be >= 0")
        self.__height = val

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """returns the printable representation of a rectangle using #"""
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle = []
        for i in range(0, self.__height):
            [rectangle.append("#") for j in range(self.__width)]
            if i != self.__height - 1:
                rectangle.append("\n")
        return ("".join(rectangle))

    def __repr__(self):
        """returns the string representation of the rectangle"""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return rect
