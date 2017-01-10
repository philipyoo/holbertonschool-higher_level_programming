#!/usr/bin/python3
def element_at(my_list, idx):
    if (idx >= -len(my_list) and idx < len(my_list):
        return my_list[idx]
    else:
        return None
