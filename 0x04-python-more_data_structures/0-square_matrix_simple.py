#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    simple_square_matrix = []

    for b in matrix:
        simple_square_matrix.append(list(a ** 2 for a in b))
    return simple_square_matrix
