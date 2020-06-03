#!/usr/bin/python3
"""ADD ATTR"""


def add_attribute(obj, key, value):
    """
    ---------------------
    METHOD: ADD_ATTRIBUTE
    ---------------------
    Description:
        Checks if an __dict__ is present. If it is,
        then the value is added
    Notes:
        If failed, then raise TyperError
    Args:
        @obj: in this case, a class
        @key: key
        @value: value
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, key, value)
    else:
        raise TypeError("can't add new attribute")
