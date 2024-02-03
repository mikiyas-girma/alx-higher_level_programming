#!/usr/bin/python3

""" the module defines a class square with private instance variable """


class Square:

    """ class named Square with private instance variable size

    Args:
        size (int): a value that initializes the ``__size`` attribute

    Attributes:
        __size (int): private instance variable
    
    Raises:
        TypeError: the ``__size`` is not type of int.
        ValueError: the ``__size`` must be greater than 0.
    """

    def __init__(self, size=0):
        """ function that runs immediately just after object instantation """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
