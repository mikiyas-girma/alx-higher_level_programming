#!/usr/bin/python3
"""contains one IO function """

import json


def load_from_json_file(filename):
    """creates an object from json file """
    lines = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            lines.append(line)
    return json.JSONDecoder().decode(''.join(lines))
