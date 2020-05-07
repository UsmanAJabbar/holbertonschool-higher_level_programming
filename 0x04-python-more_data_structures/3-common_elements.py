#!/usr/bin/python3


def common_elements(set_1, set_2):

    final_list = []

    for specific_elements in set_1 and set_2:
        if specific_elements in set_1 and set_2:
            final_list.append(specific_elements)
    return final_list
