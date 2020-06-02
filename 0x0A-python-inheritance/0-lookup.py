#!/usr/bin/python3
def lookup(obj):
    """
    --------------
    METHOD: LOOKUP
    --------------
    Description:
        Function that looks up all the attributes and
        methods associated with an object.
    Args:
        @obj: object imported from main
    --------------
    """
    return dir(obj)
