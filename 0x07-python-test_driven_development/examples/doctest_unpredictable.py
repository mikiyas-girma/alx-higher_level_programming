class MyClass:
    pass


def unpredictable(obj):
    """
    Returns a new list containing obj.

    >>> unpredictable(MyClass())
    [<doctest_unpredictable.MyClass object at 0x7f57e7be0220>]
    """
    return [obj]
