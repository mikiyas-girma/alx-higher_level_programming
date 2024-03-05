#!/usr/bin/python3
"""the module contain a class BaseGeometry"""


class BaseGeometry:
    """
    a class `BaseGeometry` that have unimplemented area method.

    Raises:
         Exception: when the method called prints area is not implemented
    """
    def area(self):
        raise Exception('area() is not implemented')
