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
    if type(size) not in [float, int]:
        raise TypeError("size must be an integer")

    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    size = int(size)  # Get rid of trailing decimal points

    # Print Square
    for height in range(size):
        if size == 0:
            break
        print("#" * size, end="")
        print()
