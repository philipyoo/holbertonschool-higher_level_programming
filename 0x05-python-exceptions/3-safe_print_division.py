#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        x = a / b
    except ZeroDivisionError:
        x = None
    finally:
        print("Inside result: {}".format(x))
        return x
