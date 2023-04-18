#!/usr/bin/python3
# rectangle.py
"""Defines a Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Describes a Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiates a new Rectangle object.

        Args:
            width (int): width of new Rectangle
            height (int): height of new Rectangle
            x (int): x co-ordinate of new Rectangle
            y (int): y co-ordinate of new Rectangle
            id (int): id of new Rectangle from Base class
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Get width of Rectangle"""
        return self.__width

    @width.setter
    def width(self, val):
        """updates the width of a Rectangle"""
        if not isinstance(val, int):
            raise TypeError("width must be an integer")
        if val <= 0:
            raise ValueError("width must be > 0")
        self.__width = val

    @property
    def height(self):
        """Get height of rectangle"""
        return self.__height

    @height.setter
    def height(self, val):
        """updates the height of a Rectangle"""
        if not isinstance(val, int):
            raise TypeError("height must be an integer")
        if val <= 0:
            raise ValueError("height must be > 0")
        self.__height = val

    @property
    def x(self):
        """get x co-ordinate of Rectangle"""
        return self.__x

    @x.setter
    def x(self, val):
        if not isinstance(val, int):
            raise TypeError("x must be an integer")
        if val < 0:
            raise ValueError("x must be >= 0")
        self.__x = val

    @property
    def y(self):
        """get y co-ordinate of Rectangle"""
        return self.__y

    @y.setter
    def y(self, val):
        if not isinstance(val, int):
            raise TypeError("y must be an integer")
        if val < 0:
            raise ValueError("y must be >= 0")
        self.__y = val

    def area(self):
        """calculate the area of a rectangle"""
        return self.width * self.height

    def display(self):
        """prints Rectangle instance with the # character"""

        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")
