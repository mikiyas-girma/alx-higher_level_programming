#!/usr/bin/python3
"""contains one function used
    in IO functions
"""
import json


def from_json_string(my_str):
    """converts json string to object and returns it"""
    return json.loads(my_str)
