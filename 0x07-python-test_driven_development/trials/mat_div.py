#!/usr/bin/python3


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
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError(messages[1])
    if not isinstance(div, (int, float)):
        raise TypeError(messages[2])
    if div == 0:
        raise ZeroDivisionError(messages[3])
    newmat = []
    newmat = [list(map(lambda x: round(x / div, 2), row)) for row in matrix]
    print(newmat)


# matrix = [[6, 4, 2], [8, 6, 4]]
# matrix = [[3]]
matrix = [[3, "9"], [12, 15, 3]]
matrix_divided(matrix, -3)
