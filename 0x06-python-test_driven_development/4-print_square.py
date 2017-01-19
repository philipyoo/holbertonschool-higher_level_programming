#!/usr/bin/python3
"""
This is the "Print Square" module.

The Print Square module prints a square using "#".
The argument supplied should determine the width/height of square.
"""


def print_square(size):
    """Print a perfect square given a valid int or float argument.
    """
    if not isinstance(size, (int, float)) or isinstance(size, bool):
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(int(size)):
        print("#" * int(size))
