#!/usr/bin/python3
import json
"""contains one function """


def from_json_string(my_str):
    """converts json string to object and returns it"""
    return json.loads(my_str)
