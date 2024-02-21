#!/usr/bin/python3

def add_integer(a, b=98):
    """this function returns the sum of its arguments"""

    if not a or (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError('b must be an integer')
    return int(a) + int(b)
