#!/usr/bin/python3
# 8-multiple_returns.py
# Brennan D Baraban

def multiple_returns(sentence):
    """Returns a tuple with the length of a string and its first character"""
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
