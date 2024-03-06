#!/usr/bin/python3
"""the module inverts builtin implementation"""


class MyInt(int):
    """the class contains function that inverts builtin 
        implementation of == and !="""
    def __init__(self, param1):
        self.param1 = param1

    def __eq__(self, param1):
        return self.param1 != param1

    def __ne__(self, param1):
        return self.param1 == param1
