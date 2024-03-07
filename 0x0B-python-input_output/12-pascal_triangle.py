#!/usr/bin/python3
"""the module contains one function called ``pascal_triangle()``"""


def pascal_triangle(n):
    """displays pascals triangle with size n"""

    if n <= 0:
        return []

    triangle = [[]]
    while len(triangle) != n:
        tri = triangle[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tri.append(tri[i] + tri[i + 1])
        tmp.append(1)
        triangle.append(tmp)
    return triangle
