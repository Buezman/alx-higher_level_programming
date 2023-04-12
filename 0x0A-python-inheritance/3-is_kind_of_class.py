#!/usr/bin/python3
# 3-is_kind_of_class.py
"""Describes a function to validate an instance or inherited class"""


def is_kind_of_class(obj, a_class):
    """Checks if obj is an instance of or inherits a_class.

    Args:
        obj (any): object to be checked
        a_class (type): class to be checked against
    Returns:
        If obj is instance or inherits from a_class - True
        Otherwise - False
    """
    return (isinstance(obj, a_class))
