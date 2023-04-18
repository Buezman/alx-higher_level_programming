#!/usr/bin/python3
# base.py
"""Base class"""
import json


class Base:
    """Base class for project.

    Attributes:
        __nb_objects (int): number of instantiated Bases
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """initialize a new base object.

        Args:
            id (int): id of new base
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
