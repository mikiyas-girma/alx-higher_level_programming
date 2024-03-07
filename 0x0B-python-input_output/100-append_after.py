#!/usr/bin/python3
"""contains one function ``append_after()``"""


def append_after(filename="", search_string="", new_string=""):
    """appends a new_string to a file after a line containing
        search_string"""

    with open(filename, mode='+r', encoding='utf-8') as f:
        line_list = []
        while True:
            line = f.readline()
            if line == "":
                break
            line_list.append(line)
            if search_string in line:
                line_list.append(new_string)

        f.writelines(line_list)
