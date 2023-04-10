#!/usr/bin/python3
# 1-safe_print_integer.py

def safe_print_integer(value):
    """Prints an integer.

    Args:
        value (int): integer to be printed
    Returns: On error false, else true
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
