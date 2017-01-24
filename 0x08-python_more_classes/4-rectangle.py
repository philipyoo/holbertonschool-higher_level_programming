#!/usr/bin/python3
"""
This is the "Rectangle"  module.

This module provides a Rectangle class.
"""


class Rectangle:
    """A Rectangle class with attributes width and height, and
    methods area, perimeter, print, str, and repr.
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __str__(self):
        total = ""
        for i in range(self.__height):
            total += ("#" * self.__width)
            if i is not self.__height - 1:
                total += "\n"
        return total

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width is 0 or self.__height is 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)
