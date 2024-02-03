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

    def __init__(self, position=(0, 0),  size=0):
        """initializes the square object"""
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Retrieves the position of the square

        Returns:
            tuple: type position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """updates the position of the square

        Args:
            value(tuple): the position to be assigned to the square
        """
        if isinstance(value, tuple):
            if isinstance(value[0], int) and isinstance(value[1], int):
                if value[0] >= 0 and value[1] >= 0:
                    self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """ function that prints '#' symbol with size of the square based
         on its position
           """
        if self.__size > 0:
            print('{}'.format('\n' * self.__position[1]), end='')
            for i in range(self.__size):
                print('{}{}'.format(' ' * self.__position[0],
                                    '#' * self.__size))
        else:
            print()
