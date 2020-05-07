#!/usr/bin/python3


def search_replace(my_list, search, replace):
    if not my_list:
        return None

    new_list = my_list[:]

    for indexes in range(len(my_list)):
        if new_list[indexes] == search:
            new_list[indexes] = replace

    return new_list
