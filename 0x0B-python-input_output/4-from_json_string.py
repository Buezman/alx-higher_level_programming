#!/usr/bin/python3
# 4-from_json_string.py
"""Defines a function that converts a json to string"""
import json


def from_json_string(my_str):
    """creates a string representation of a JSON.

    Args:
        my_str (str): JSON to be converted

    Returns: string representation of my_str
    """
    return json.loads(my_str)
