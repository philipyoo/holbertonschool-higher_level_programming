#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = list(tuple_a) + [0]*2
    b = list(tuple_b) + [0]*2
    c = [x + y for x, y in zip(a, b)]
    return tuple(c[0:2])
