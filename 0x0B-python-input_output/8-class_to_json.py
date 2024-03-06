#!/usr/bin/python3
"""contains one function ``class_to_json()``"""


def class_to_json(obj):
    """returns dictionary representation of ds
        that are suitable for json serialization"""
    return obj.__dict__
