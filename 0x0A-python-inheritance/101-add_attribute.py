#!/usr/bin/python3
"""this module contains one ``add_attribute()`` function"""


def add_attribute(obj, attr, value):
    if hasattr(obj, '__dict__'):
        obj.__setattr__(attr, value)
    else:
        raise TypeError("can't add new attribute")
