#!/usr/bin/python3
"""the module contains a single class"""


class LockedClass:
    """restricts instantiation unless instance
        name is `first_name`
    """
    __slots__ = ['first_name']
