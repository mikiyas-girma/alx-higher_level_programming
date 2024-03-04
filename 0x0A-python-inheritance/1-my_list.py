#!/usr/bin/python3
"""a simple module with one function inside MyList class"""


class MyList(list):
    """this is a child of list class"""

    def print_sorted(self):
        """prints the list in sorted way ascendingly"""
        print(sorted(self))
