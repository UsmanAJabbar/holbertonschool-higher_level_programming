#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    new_matrix = []
    index = 0

    for elements in matrix:
        new_matrix.append(list(map(lambda elements: elements ** 2, elements)))
    return new_matrix
