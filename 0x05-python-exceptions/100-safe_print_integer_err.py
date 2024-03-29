#!/usr/bin/python3
# 100-safe_print_integer_err.py

import sys


def safe_print_integer_err(value):
    """Prints an integer.

    Args:
        value (int): integer to be printed

    Returns: True if value is an integer, else False
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return False
