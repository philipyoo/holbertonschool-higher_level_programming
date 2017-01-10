#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if (-len(my_list) <= idx < len(my_list)):
        my_list[idx] = element
    return my_list
