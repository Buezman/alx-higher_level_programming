#!/usr/bin/python3
# 100-my_int.py
"""Describes a class that inherits from int"""


class MyInt(int):
    """Rebel class"""

    def __eq__(self, value):
        """Inverts the equals (==) operator"""
        return self.real != value

    def __ne__(self, value):
        """Inverts the not equals (!=) operator"""
        return self.real == value
