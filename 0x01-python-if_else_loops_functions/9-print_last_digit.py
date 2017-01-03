#!/usr/bin/python3
def print_last_digit(number):
    tmp = int(repr(number)[-1])
    print("{}".format(tmp), end="")
    return tmp
