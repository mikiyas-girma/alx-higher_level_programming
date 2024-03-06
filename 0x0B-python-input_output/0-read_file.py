#!/usr/bin/python3
"""module that contains ``read_file()`` function"""


def read_file(filename="testfile.txt"):
    """reads and prints contents in a file specified"""
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read())
