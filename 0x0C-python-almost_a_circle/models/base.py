#!/usr/bin/python3
"""this module will be used as a base class"""


class Base:
    """this class represents as a base for all other classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initializes a new base with unique id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
