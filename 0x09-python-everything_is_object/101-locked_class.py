#!/usr/bin/python3
# 101-locked_class.py
"""Defines a locked class"""

class LockedClass:
    """
    Prevents a user from from dynamically creating
    new instance attributes, except if the new
    instance attribute is called first_name
    """


    __slots__ = ["first_name"]
