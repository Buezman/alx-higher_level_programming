#!/usr/bin/python3
# 2-is_same_class.py
"""Defines a function for validating class type"""


def is_smae_class(obj, a_class):
    """Checks if obj is instance of given class types.

    Args:
        obj (any): object to check
        a_class (type): class to validate the object instance against
    Returns:
        True is obj is instance of a_class,
        Otherwise - False
    """
    return (type(obj) == a_class)
