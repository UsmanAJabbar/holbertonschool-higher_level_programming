#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    if my_list:
        new_list = my_list[:]

        # Check if idx exists
        if idx < 0:
            return(new_list)

        elementcount = len(my_list) - 1
        if idx > elementcount:
            return(new_list)

        # idx definitely exists, return modified list
        else:
            new_list[idx] = element
            return(new_list)
