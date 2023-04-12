#!/usr/bin/python3
# 1-my_list.py
"""Describes a class that inherits from list"""


class MyList(list):
    """Inherited class from list"""

    def print_sorted(self):
        """Prints a list in sorted-ascending order"""
        print(sorted(self))
