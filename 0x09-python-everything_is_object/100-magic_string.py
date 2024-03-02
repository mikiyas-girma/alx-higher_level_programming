#!/usr/bin/python3
def magic_string():
    magic_string.n, x = (magic_string.__dict__.get('n', 0) + 1, ', BestSchool')
    return '{:s}{:s}'.format(x[2:], x * (magic_string.n - 1))