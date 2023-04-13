#!/usr/bin/python3
# 9-student.py
"""Defines a student class"""


class Student:
    """Student class representation"""

    def __init__(self, first_name, last_name, age):
        """Instantiates a new Student.

        Args:
            first_name (str): studemt's firstname
            last_name (str): studen'ts lastname
            age (int): student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns a dictionary representation of a student object"""
        return self.__dict__
