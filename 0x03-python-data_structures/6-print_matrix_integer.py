#!/usr/bin/python3
# 6-print_matrix_integer.py
# Brennan D Baraban

def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers"""
    for elm in matrix:
        print(" ".join("{:d}".format(i) for i in elm))
