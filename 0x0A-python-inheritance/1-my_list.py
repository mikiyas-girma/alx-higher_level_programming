#!/usr/bin/python3

class MyList(list):
    """this is a child of list class"""
    def print_sorted(self):
        print(sorted(self))
