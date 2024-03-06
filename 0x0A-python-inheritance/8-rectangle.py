#!/usr/bin/python3
"""the module contain a class BaseGeometry
    and its subclass Rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """contains a function to instantiate a rectangle"""
    def __init__(self, width, height):
        if (self.integer_validator('width', width) and
                self('height', height)):
            self.__width = width
            self.__height = height
