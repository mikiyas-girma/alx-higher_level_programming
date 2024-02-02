#!/usr/bin/python3

""" the module defines a class square with private instance variable """


class Square:

    """ class named Square with private instance variable size

    Args:
        size (int): a value that initializes the ``__size`` attribute

    Attributes:
        __size (int): private instance variable
    """

    def __init__(self, size):
        """ function that runs immediately just after object instantation """
        self.__size = size
