#!/usr/bin/python3
# 12-pascal_triangle.py
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.
    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    result = [[1]]
    while len(result) != n:
        x = result[-1]
        tmp = [1]
        for i in range(len(x) - 1):
            tmp.append(x[i] + x[i + 1])
        tmp.append(1)
        result.append(tmp)
    return result
