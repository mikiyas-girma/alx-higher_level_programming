#!/usr/bin/python3
"""the module imports Rectangle class and use its attributes"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """inherits from the class ``Rectangle`` and instantiate it"""
    def __init__(self, size):
        """init function used  for instantiating itself also
            its parent class """
        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
