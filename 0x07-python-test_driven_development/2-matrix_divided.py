#!/usr/bin/python3
"""Matrix Divided"""


def matrix_divided(matrix, div):
    """
    ----------------------
    METHOD: MATRIX DIVIDED
    ----------------------
    Description:
        Divides all the int/float elements in a
        matrix by a certain number defined
        by div.
    Exceptions:
        Checks the existence of div and matrix.
        Raises exceptions if either one fails or
        elements in matrix aren't floats or integers
    Args:
        matrix: imports the matrix from the main
                file.
        div:    number that defines what each element
                int a matrix should be divided with.
    """

    matrixerror = "matrix must be a matrix (list of lists) of integers/floats"
    emptyargs = "matrix_divided() missing 2 required positional arguments\
: 'matrix' and 'div'"

    # EDGE CASES / RAISE ERRORS
    if matrix is None and div is None:
        raise TypeError(emptyargs)
    if matrix is None or type(matrix) is not list:
        raise TypeError(matrixerror)

    if type(div) not in [float, int]:
        raise TypeError("div must be a number")
    if div is None or div == 0:
        raise ZeroDivisionError("division by zero")

    # VALIDATE SIZE OF MATRIX + ELEMENT DATA TYPES
    listcount = len(matrix)     # Find the number of individual lists

    if listcount < 1:           # Should fail on [] not on [[1], [2]]
        raise TypeError(matrixerror)

    elementcount = 0            # Initialized to 0 for the for loop
    for lists in matrix:        # Finds the number of elements the matrix
        if type(lists) is not list:                 # type(list) check
            raise TypeError(matrixerror)
        for elements in lists:
            if type(elements) not in [float, int]:  # Validates data types
                raise TypeError(matrixerror)
            elementcount += 1

    if elementcount % listcount != 0:
        raise TypeError("Each row of the matrix must have the same size")

    # START DIVIDING AND RETURN THE NEW LIST
    div_mat = []
    div = int(div)
    for nums in matrix:
        div_mat.append(list(map(lambda nums: round(nums / div, 2), nums)))

    return div_mat
