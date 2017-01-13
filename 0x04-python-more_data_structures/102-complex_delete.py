#!/usr/bin/python3
def complex_delete(my_dict, value):
    copy = my_dict.copy()
    for k, v in copy.items():
        if value in v:
            del my_dict[k]
    return my_dict
