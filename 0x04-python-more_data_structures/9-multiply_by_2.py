#!/usr/bin/python3
# 9-multiply_by_2.py
# Brennan D Baraban <375@holbertonschool.com>

def multiply_by_2(a_dictionary):
    """Return a new dictionary with all values multiplied by 2."""
    return ({k: a_dictionary[k] * 2 for k in a_dictionary})
