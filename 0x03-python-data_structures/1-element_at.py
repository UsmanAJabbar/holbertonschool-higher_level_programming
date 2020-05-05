#!/usr/bin/python3


def element_at(my_list, idx):
    # If index doesn't exit, return none
    if idx < 0:
        return None

    elementcount = len(my_list) - 1

    if idx > elementcount:
        return None

    # If index does exist, return element
    return my_list[idx]
