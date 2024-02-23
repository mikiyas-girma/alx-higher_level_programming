#!/usr/bin/python3
"""this module contains only one ``print_square()`` function"""


def print_square(size):
    """this function prints a square with '#' based on its size"""
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')
    for i in range(size):
        print('#' * size)
