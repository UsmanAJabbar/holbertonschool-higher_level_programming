#!/usr/bin/python3

# This function returns a copy of the original
# list with modified data at a specific index
# If the index doesn't exit, returns a copy
# of the original list

def new_in_list(my_list, idx, element):
    new_list = my_list[:]

    # Check if idx exists
    if idx < 0:
        return(new_list)

    elementcount = len(my_list)
    if idx > elementcount:
        return(new_list)

    # idx definitely exists, return modified list
    else:
        new_list[idx] = element
        return(new_list)
