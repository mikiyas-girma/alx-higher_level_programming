#!/usr/bin/python3
"""
this module contains one simple function say_my_name()
"""


def say_my_name(first_name, last_name=""):
    """
    this function prints the first name and last name that is passed
    to it
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print(f'My name is {first_name} {last_name}')
