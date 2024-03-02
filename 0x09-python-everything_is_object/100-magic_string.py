#!/usr/bin/python3
def magic_string():
    magic_string.n, tu = (magic_string.__dict__.get('n', 0) + 1, ', BestSchool')
    return '{:s}{:s}'.format(tu[2:], tu * (magic_string.n - 1))
