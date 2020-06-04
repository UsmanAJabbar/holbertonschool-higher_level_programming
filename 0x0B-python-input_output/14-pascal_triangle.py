#!/usr/bin/python3
"""PASCAL TRIANGLE"""


def pascal_triangle(n):

#   1 is always gonna be on the outside
#   pull the prev list and being appending the
#   values in it using a 2 index window and make sure
#   that we end with 1 at the end.

    matrix = []
    if n <= 0:
        return matrix

    prev = [1]
    for elements in range(n):
        list_builder = [1]      # New list always starts with 1

        for i in range(elements):   # Keep a record of elements
            if (i + 1) == elements:     # If we are at the end
                list_builder.append(prev[i]) # Copied the last 1
            else:
                list_builder.append(prev[i] + prev[i + 1])

        prev = list_builder # Keep a record of prev
        matrix.append(list_builder) # Append the list to matrix

    return matrix
