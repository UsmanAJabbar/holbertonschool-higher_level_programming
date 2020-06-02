#!/usr/bin/python3
def inherits_from(obj, a_class):
    """
    -------------------------
    METHOD: IS KIND OFF CLASS
    -------------------------
    Description:
        Verifies whether two objects given are of the
        same class.
    Args:
        @obj: object
        @a_class: class
    """
    return isinstance(obj, a_class) and type(obj) != a_class
