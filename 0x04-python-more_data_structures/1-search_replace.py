#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list = []
    for a in my_list:
        if a == search:
            list.append(replace)
        else:
            list.append(a)
    return list
