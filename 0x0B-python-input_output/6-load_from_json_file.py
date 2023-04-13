#!/usr/bin/python3
# 6-load_from_json_file.py
"""Defines a function that an object from a JSON file"""
import json


def load_from_json_file(filename):
    """Creates a object from JSON file.

    Args:
        filename (str): name of JSON file
    """
    with open(filename) as f:
        return json.loads(f)
