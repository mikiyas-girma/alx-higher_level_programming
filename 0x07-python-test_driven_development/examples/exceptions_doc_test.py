"""
this is "exceptions_doc_test" module.

the module supplies  functions , divide() and add(). for example

# >>> divide(4, 2)
# 2.0
>>> add(1, None)
Traceback (most recent call last):
    ...
TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'
"""


def divide(a, b):
    """
    Function to divide two numbers.

    >>> divide(10, 0)
    Traceback (most recent call last):
        ...
    ZeroDivisionError: division by zero

    >>> divide(10, 2)
    5.0
    """

    return a / b


def add(a, b):
    """
    Function to add two numbers.

    >>> add(1, 2)
    3
    """
    return a + b


if __name__ == "__main__":
    import doctest
    doctest.testmod()
