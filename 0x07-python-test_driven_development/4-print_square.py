#!/usr/bin/python3
def print_square(size):
    """
    --------------------
    METHOD: PRINT SQUARE
    --------------------
    Description:
        Prints a square with the size defined
        by @size.

    Exceptions:
        Validates data before printing it out
        Raises an exception on bad input

    Args:
        @size: size defined by main
    """
    if type(size) is not int or type(size) is not float:
        raise TypeError("size must be an integer")

    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    if type(size) is int and size < 0:
        raise ValueError("size must be >= 0")

    size = int(size)  # Get rid of trailing decimal points

    # Print Square
    for height in range(size):
        if size == 0:
            break
        print("#", end="") * size
        print()
