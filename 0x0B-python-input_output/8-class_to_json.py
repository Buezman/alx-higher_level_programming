#!/usr/bin/python3
# 8-class_to_json.py
"""Defines a class to JSON function"""


def class_to_json(obj):
    """Returns the dictionary representation of a data structure

    Args:
        obj (str): data structure
    """
    return obj.__dict__
