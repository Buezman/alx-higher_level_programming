#!/usr/bin/python3
# 5-save_to_json_file.py
"""Defines a function that writes a JSOn to a file"""
import json


def save_to_json_file(my_obj, filename):
    """Writes JSON object to file

    Args:
        my_obj (str): JSON object
        filename (str): file to write object to
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
