#!/usr/bin/python3
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

    # EDGE CASES / RAISE ERRORS
    if type(matrix[0]) is not list:
        raise TypeError(matrixerror)

    if type(div) not in [float, int]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # VALIDATE SIZE OF MATRIX + ELEMENT DATA TYPES
    listcount = len(matrix)     # Find the number of individual lists
    elementcount = 0            # Initialized to 0 for the for loop
    for lists in matrix:        # Finds the number of elements the matrix
        for elements in lists:
            if type(elements) not in [float, int]:  # Validates data types
                raise TypeError(matrixerror)
            elementcount += 1

    if elementcount % listcount != 0:
        raise TypeError("Each row of the matrix must have the same size")

    # START DIVIDING AND RETURN THE NEW LIST
    divided_matrix = []

    for elements in matrix:
        divided_matrix.append(list(map(lambda elements: round(elements / div, 2), elements)))

    return divided_matrix
