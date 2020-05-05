#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    elementcount = len(my_list) - 1

    for elements in range(elementcount, -1, -1):
        print("{:d}".format(my_list[elements]))
