import doctest_private_tests_external
__test__ = {
    'numbers': """
>>> my_function(2 ,3)
6
""",

    'strings': """
>>> my_function('a', 3)
'aaa'
""",

    'external': doctest_private_tests_external
}


def my_function(a, b):
    """Returns a * b
    """
    return a * b


if __name__ == "__main__":
    import doctest
    doctest.testmod()
