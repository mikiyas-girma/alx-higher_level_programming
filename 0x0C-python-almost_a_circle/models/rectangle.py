#!/usr/bin/python3
"""this module imports parent class Base"""

from models.base import Base


class Rectangle(Base):
    """inherits from parent class 'Base' """
    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes the object of a class with id from parent class"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """returns width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width"""
        self.__width = value

    @property
    def height(self):
        """returns height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height"""
        self.__height = value

    @property
    def x(self):
        """returns the value x"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the value for x"""
        self.__x = value

    @property
    def y(self):
        """returns the value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the value of y"""
        self.__y = value
