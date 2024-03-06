#!/usr/bin/python3
"""the module imports two functions to
    load from and save to json file"""

from sys import argv
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


try:
    json_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    json_list = []

for arg in argv[1:]:
    json_list.append(arg)

save_to_json_file(json_list, "add_item.json")
