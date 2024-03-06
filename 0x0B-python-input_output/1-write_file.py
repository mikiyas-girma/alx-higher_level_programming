#!/usr/bin/python3
"""the contains one function ``write_file()``"""


def write_file(filename="", text=""):
    """function to write a text to a file"""
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(str(text))
