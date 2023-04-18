#!/usr/bin/python3
# base.py
"""Base class"""
import json
import csv


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

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes JSON string of list_objs to a file.

        Args:
            cls (string): filename
            list_objs (list): list of objects
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
            else:
                dicts = [i.to_dictionary() for i in list_objs]
                f.write(Base.to_json_string(dicts))

    @classmethod
    def from_json_string(json_string):
        """Returns list of JSON string representation

        Args:
            json_string (string): JSON string

        Returns:
            if json_string is None or empty - []
            else - a list representation of json_string
        """
        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)
