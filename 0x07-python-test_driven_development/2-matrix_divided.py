#!/usr/bin/python3
"""
this module contains one functions that divides
items in a list of list with a given number
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number
    """
    messages = ("matrix must be a matrix (list of lists) of integers/floats",
                "Each row of the matrix must have the same size",
                "div must be a number",
                "division by zero")

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(messages[0])
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(messages[0])
    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError(messages[0])
    if not all(len(row) for row in matrix):
        raise TypeError(messages[1])
    if not isinstance(div, (int, float)):
        raise TypeError(messages[2])
    if div == 0:
        raise ZeroDivisionError(messages[3])
    newmat = []
    mod = list(map(lambda x: round(x / div, 2), row) for row in matrix)
    newmat.append(mod)

    return newmat
