#!/usr/bin/python3
# 0-read_file.py
"""Defines a function that reads a file"""


def read_file(filename=""):
    """Reads a file and prints to stdout

    Args:
        filename (string): name of file to be read
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
