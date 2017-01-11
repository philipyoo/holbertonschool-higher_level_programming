#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    new_list = [:]
    if new_list is None:
        return new_list
    if idx < len(new_list):
        del new_list[idx]
    return new_list
