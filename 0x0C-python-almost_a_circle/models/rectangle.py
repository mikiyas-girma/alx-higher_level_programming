#!/usr/bin/python3
"""this module imports parent class Base"""

from models.base import Base


class Rectangle(Base):
    """inherits from parent class 'Base' """
    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes the object of a class with id from parent class"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

        super().__init__(id)

    @property
    def width(self):
        """returns width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """returns height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """returns the value x"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the value for x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """returns the value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the value of y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returs area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """represents rectangle with '#' """
        res = []
        [print() for y in range(self.__y)]
        for i in range(self.__height):
            [res.append(' ') for x in range(self.__x)]
            [res.append('#') for j in range(self.__width)]
            res.append('\n')
        print(''.join(res), end='')

    def __str__(self):
        """returns custom representation for instance of a class"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
                self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args):
        """assigns argument to each attribute"""
        a = 0
        for arg in args:
            if a == 0:
                if arg is None:
                    self.__init__(self.width, self.height, self.x, self.y)
                else:
                    self.id = arg
            elif a == 1:
                self.width = arg
            elif a == 2:
                self.height = arg
            elif a == 3:
                self.x = arg
            elif a == 4:
                self.y = arg
            a += 1
