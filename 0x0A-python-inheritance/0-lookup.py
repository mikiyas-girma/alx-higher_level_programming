#!/usr/bin/python3
"""the module contain one simple ``lookup()`` function"""


def lookup(obj):
    """returns a list of all its attributes"""
    return (dir(obj))
