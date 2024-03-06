#!/usr/bin/python3
"""module containing one function"""


def append_write(filename="", text=""):
    """appends text to file and returns the no of characters added"""
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(str(text))
