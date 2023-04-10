#!/usr/bin/python3
# 101-safe_function.py

import sys


def safe_function(fct, *args):
    """Safely executes a function.

    Args:
        fct (func): pointer to a function
        args: arguments for fct

    Returns:
        If no error - result of fct
        On error - None
    """
    try:
        result = fct(*args)
        return result
    except Exception:
        print("Exceptionr {}".format(sys.exc_info()[1]), file=sys.stderr)
        return None
