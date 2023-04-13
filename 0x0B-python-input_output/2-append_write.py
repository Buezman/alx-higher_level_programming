#!/usr/bin/python3
# 2-append_write.py
"""Defines a function that appends a text to end of file"""


def append_write(filename="", text=""):
    """appends text to end of UTF-8 file.

    Args:
        filename (str): name of file to be appended to
        text (str): text to be appended

    Returns: number of characters appended
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
