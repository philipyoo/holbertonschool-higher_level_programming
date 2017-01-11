#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if not my_list:
        return my_list
    if 0 <= idx < len(my_list):
        del my_list[idx]
    return my_list
