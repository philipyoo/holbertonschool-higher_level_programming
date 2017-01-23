#!/usr/bin/python3
import dis
import math

class MagicClass:
    def __init__(self, radius):
        self.__radius = 0

        if type(radius) is not int or type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    def area(self):
        return self.__radius ** 2 * math.pi

    def circumference():
        return 2 * math.pi * self.__radius

"""
    @radius.setter
    def radius(self, value):
        if type(radius) is not int or type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = value
"""

dis.dis(MagicClass)
