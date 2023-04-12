#!/usr/bin/python3
# 6-base_geometry.py
"""Defines a base class"""


class BaseGeometry:
    """Base Geometry class"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates a value as an integer.

        Args:
            name (string): name of parameter
            value (int): integer value of parameter

        Raises:
            TypeError if value is not an int
            ValueError if value is <= 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
