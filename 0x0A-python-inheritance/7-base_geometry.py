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

    def integer_validator(self, name, value):
        """validates that a value must be an integer greater than 0"""
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
