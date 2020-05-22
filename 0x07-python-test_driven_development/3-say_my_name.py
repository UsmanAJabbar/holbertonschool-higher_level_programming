#!/usr/bin/python3
"""'YA GAAD DAMN RIGHT'"""


def say_my_name(first_name, last_name=""):
    """
    -------------------
    METHOD: SAY MY NAME
    -------------------
    Description:
        Strikes Heisenberg nostalgia back into you.
        Otherwise, it prints out the first
        name and last name defined by the
        two variables.

    Exceptions:
        Checks if first_name has been defined.
        Checks if first_name and last name are strings.
        If last_name hasn't been defined, last_name
        defaults to an empty string

    Args:
        first_name = first name
        last_name = last name
    """
    # Checks if variables are strings
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
