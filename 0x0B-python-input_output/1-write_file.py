#!/usr/bin/python3
# 1-write_file.py
"""Defines a function that writes a string to a file"""


def write_file(filename="", text=""):
    """Writes text to file.

    Args:
        filename (string): file to be written to
        text (string): string to be written to file

    Returns: number of characters written to file
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
