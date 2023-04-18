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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSON string representation of a list of dictionaries

        Args:
            list_dictionaries (list): list of dictionaries

        Returns:
            if list_dictionaries is null or empty - "[]"
            else - JSON string of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
