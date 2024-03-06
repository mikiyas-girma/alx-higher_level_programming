#!/usr/bin/python3
"""the module contain a class BaseGeometry
    and its subclass Rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """contains a function to instantiate a rectangle"""
    def __init__(self, width, height):
        if self.integer_validator('width', width):
            self.__width = width
        if self.integer_validator('height', height):
            self.__height = height
