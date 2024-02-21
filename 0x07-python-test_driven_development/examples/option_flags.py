def is_even(num):
    """
    Function to check if a number is even.

    >>> is_even(2)  # doctest: +DONT_ACCEPT_TRUE_FOR_1
    1
    >>> is_even(3)
    False
    """
    return num % 2 == 0


if __name__ == "__main__":
    import doctest
    doctest.testmod(optionflags=doctest.DONT_ACCEPT_TRUE_FOR_1)
