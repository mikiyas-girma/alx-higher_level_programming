#!/usr/bin/python3
"""the module contain a class BaseGeometry
    and its subclass Rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """contains a function to instantiate a rectangle"""
    def __init__(self, width, height):
        """calls __init__ of parent class and instantiate its object"""
        super().__init__()
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        """returns area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """string representation of the rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
