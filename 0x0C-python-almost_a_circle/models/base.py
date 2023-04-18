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

    @staticmethod
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
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes set

        Args:
            cls (class): class of object
            **dictionary (dict): dictionary of arguments
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new_cls = cls(1, 1)
            else:
                new_cls = cls(1)
            new_cls.update(**dictionary)
            return new_cls

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from a file.

        Args:
            cls (class): class type
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as f:
                dicts = Base.from_json_string(f.read())
                return [cls.create(**d) for d in dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save a list of instances to CSV file

        Args:
            cls (class): class type
            list_objs (list): list of instances
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    attr = ["id", "width", "height", "x", "y"]
                else:
                    attr = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=attr)
                for o in list_objs:
                    writer.writerow(o.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    attr = ["id", "width", "height", "x", "y"]
                else:
                    attr = ["id", "size", "x", "y"]
                dic = csv.DictReader(csvfile, fieldnames=attr)
                dic = [dict([k, int(v)] for k, v in d.items()) for d in dic]
                return [cls.create(**d) for d in dic]
        except IOError:
            return []
