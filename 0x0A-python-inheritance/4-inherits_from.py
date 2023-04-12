#!/usr/bin/python3
# 4-inherits_from.py
"""Describes a function that validates a an object as a subclass"""


def inherits_from(obj, a_class):
    """Checks if obj is instance of subclass of a_class.

    Args:
        obj (any): object to validate
        a_class (type): class to validate against
    
    Returns:
        If class type of obj is subclass of a_class - True
        Otherwise - False
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
