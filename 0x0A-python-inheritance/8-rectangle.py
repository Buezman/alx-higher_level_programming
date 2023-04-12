#!/usr/bin/python3
# 8-rectangle
"""Defines a Rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Describes the Rectangle shape"""

    def __init__(self, width, height):
        """Initializes a new Rectangle

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
