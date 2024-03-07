#!/usr/bin/python3
"""this module imports parent class Base"""

Base = __import__('base').Base


class Rectangle(Base):
    """inherits from parent class 'Base' """
    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes the object of a class with id from parent class"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)
