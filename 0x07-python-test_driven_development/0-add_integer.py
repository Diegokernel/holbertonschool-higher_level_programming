#!/usr/bin/python3
""" add_integer
    function
    adds two numbers
    a, b
"""


def add_integer(a, b=98):
    """Returns a + b.
       checks typeErrors for a and b
    """
if not isinstance(a, (float, int)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (float, int)):
        raise TypeError("b must be an integer")
    return int(a + b)
