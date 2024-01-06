#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 | idx > len(my_list):
        return
    print("Element at index {:d} is {}".format(idx, my_list[idx]))
