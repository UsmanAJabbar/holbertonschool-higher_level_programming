#!/usr/bin/python3

# This function is supposed to return the element
# at a specific index

def element_at(my_list, idx):
    # If index doesn't exit, return none
    if idx < 0:
        return()

    elementcount = len(my_list)

    if idx > elementcount:
        return()

    # If index does exist, return element
    return(my_list[idx])
