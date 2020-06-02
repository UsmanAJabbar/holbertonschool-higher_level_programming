#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """
    ---------------------
    METHOD: KIND OF CLASS
    ---------------------
    Description:
        Verifies whether two objects given are of the
        same class.
    Args:
        @obj: object
        @a_class: class
    """
    return True if isinstance(obj, a_class) else False
