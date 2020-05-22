#!/usr/bin/python3
"""ADD INTEGER"""


def add_integer(a, b=98):
    """
    -------------------
    METHOD: ADD INTEGER
    -------------------
    Description:
        Adds two integers/floats.
    Exceptions:
        If a or b is a float, then the float must be
        would be casted an as integer before the return's
        generated.
    Args:
        a = Requires user input
        b = If not defined, defaults to 98
    """

    # Check if we have good inputs, a must exist to continue
    if a is None:
        raise TypeError("add_integer() missing 1 required positional argument: 'a'")

    # If a exists, check data types
    if type(a) is not int and type(a) is not float:
            raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
            raise TypeError("b must be an integer")

    # If they're floats/ints, cast and return ints
    return int(a) + int(b)
