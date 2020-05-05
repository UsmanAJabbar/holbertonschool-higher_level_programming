#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    elementcount = len(my_list)
    reversed_list = my_list[::-1]

    for elements in range(0, elementcount):
        print("{:d}".format(reversed_list[elements]))
