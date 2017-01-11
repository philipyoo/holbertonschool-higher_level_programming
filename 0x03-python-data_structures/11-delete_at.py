#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if my_list is None:
        return my_list
    if idx < len(my_list):
        del my_list[idx]
    return my_list
