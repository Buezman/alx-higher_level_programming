#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []

    for x in matrix:
        inner = []
        for y in x:
            inner.append(y * y)
        result.append(inner)
    return result
