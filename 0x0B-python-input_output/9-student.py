#!/usr/bin/python3
"""contains a class Student"""


class Student:
    """Representation of a student"""
    def __init__(self, first_name, last_name, age):
        """initializes instance of a Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns dict representation of an instance"""
        return self.__dict__
