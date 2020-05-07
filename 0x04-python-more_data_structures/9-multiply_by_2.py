#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    # Declarations
    oxford_v1 = dict(a_dictionary)
    result = 1

    for keys in a_dictionary:
        oxford_v1[keys] = oxford_v1[keys] * 2

    return oxford_v1
