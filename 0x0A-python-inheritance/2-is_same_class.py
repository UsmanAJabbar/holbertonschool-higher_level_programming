#!/usr/bin/python3
"""I DON'T GET WHY THIS IS A REQ"""


def is_same_class(obj, a_class):
    """
    ---------------------
    METHOD: IS SAME CLASS
    ---------------------
    Description:
        Verifies whether two objects given are of the
        same class.
    Args:
        @obj: object
        @a_class: class
    """
    return type(obj) == a_class
