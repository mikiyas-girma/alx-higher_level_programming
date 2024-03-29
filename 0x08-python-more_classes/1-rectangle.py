#!/usr/bin/python3
"""this module contain a simple Rectangle class"""


class Rectangle:
    """this is empty rectangle class"""
    def __init__(self, width=0, height=0):
        """initializes width and height for an instance"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """returns the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """this retrieves the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """this function sets the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
