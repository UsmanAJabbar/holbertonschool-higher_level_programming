#!/usr/bin/python3


def uniq_add(my_list=[]):

    # Declarations
    new_list = my_list[:]  # Creating a copy of the original list
    fodups = set(new_list)  # Removing Duplicates
    sum = 0  # Initializing sum to 0 for the loop

    for elements in fodups:
        sum = sum + elements

    return sum
