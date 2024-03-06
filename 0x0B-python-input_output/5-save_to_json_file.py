#!/usr/bin/python3
"""module contains one function that is
    used in IO manipulation
"""

import json


def save_to_json_file(my_obj, filename):
    """saves the json representation of an object to a file"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
