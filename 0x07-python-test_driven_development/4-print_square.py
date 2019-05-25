#!/usr/bin/python3
""" function that prints
    a square
"""

def print_square(size):
    """prints a square
       Args:
            size (int)
    """
    if not type(size) is int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("{}".format("#" * size))
