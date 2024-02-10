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
        """initializes the square object"""
        self.__size = size

    def area(self):
        """ function that computes area of the square
        Returns:
            the current area of the square
        """
        return self.__size * self.__size

    @property
    def size(self):
        """ retrieves the size of the square

        Returns:
            int: size of the square
        """
        return self.__size

    @size.setter
    def size(self, size):
        """ sets the size of the square

        Args:
            value (int): the new size of the square
        Raises:
            TypeError: the ``__size`` is not type of int.
            ValueError: the ``__size`` must be greater than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def __eq__(self, other):
        """ checks if two squares are equal

        Args:
            other (Square): the square to be compared
        Returns:
            bool: True if the two squares are equal, False otherwise
        """
        return self.__size == other.__size

    def __ne__(self, other):
        """ checks if two squares are not equal

        Args:
            other (Square): the square to be compared
        Returns:
            bool: True if the two squares are not equal, False otherwise
        """
        return self.__size != other.__size

    def __gt__(self, other):
        """ checks if the first square is greater than the second

        Args:
            other (Square): the square to be compared
        Returns:
            bool: True if the first square is greater, False otherwise
        """
        return self.__size > other.__size

    def __ge__(self, other):
        """ checks if the first square is greater or equal to the second

        Args:
            other (Square): the square to be compared
        Returns:
            bool: True if the first square is greater or equal, False otherwise
        """
        return self.__size >= other.__size

    def __lt__(self, other):
        """ checks if the first square is less than the second

        Args:
            other (Square): the square to be compared
        Returns:
            bool: True if the first square is less, False otherwise
        """
        return self.__size < other.__size

    def __le__(self, other):
        """ checks if the first square is less or equal to the second

        Args:
            other (Square): the square to be compared
        Returns:
            bool: True if the first square is less or equal, False otherwise
        """
        return self.__size <= other.__size
