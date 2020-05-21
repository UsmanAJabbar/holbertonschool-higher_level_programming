#!/usr/bin/python3
def add_integer(a, b=98):
    """
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

    if not a:
        raise TypeError("add_integer() missing 1 required positional argument: 'a'")

    if a:
        if type(a) is not int or type(a) is not float:
            raise TypeError("a must be an integer")

    if type(b) is not int or type(b) is not float:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
