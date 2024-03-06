#!/usr/bin/python3
"""contains one IO function"""
import json


def to_json_string(my_obj):
    s_obj = json.dumps(my_obj, sort_keys=True)
    return s_obj
