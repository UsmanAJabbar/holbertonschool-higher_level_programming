#!/usr/bin/python3


def number_keys(a_dictionary):
    if not a_dictionary:
        return None
    count = 0

    for keys in a_dictionary:
        count += 1

    return count
