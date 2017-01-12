#!/usr/bin/python3
def multiply_by_2(my_dict):
    new_dict = {}
    for k, v in my_dict.items():
        new_dict[k] = v * 2
    return new_dict
