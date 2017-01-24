#!/usr/bin/python3
"""
This is the "Square"  module.

This module provides a simple Square class with initialize size.
Size defaults to 0. Raise errors on invalid inputs.
"""


class Square:
    """A class that defines a square by size"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
