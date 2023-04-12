#!/usr/bin/python3
# 101-add_attribute.py
"""Defines a function to add attribues to objects"""


def add_attribute(obj, attr, val):
    """Adds new attribute to object

    Args:
        obj (any): object to add attribute
        attr (string): name of attribute
        val (any): Value of attribute

    Raises: TypeError if attribute can't be added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, val)
