#!/usr/bin/python3
# 3-to_json_string.py
"""Defines a function that converts a string to json"""
import json


def to_json_string(my_obj):
    """creates a JSON representation of an obj in string format.

    Args:
        my_obj (str): object in string format

    Returns: JSON representation of my_obj
    """
    return json.dumps(my_obj)
