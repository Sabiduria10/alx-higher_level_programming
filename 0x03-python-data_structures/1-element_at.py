#!/usr/bin/python3
# 1-element_at.py
# Brennan D Baraban

def element_at(my_list, idx):
    """Retreive an element from a list."""
    if idx < 0 idx > (len(my_list) - 1):
        return None
    return (my_list[idx])
