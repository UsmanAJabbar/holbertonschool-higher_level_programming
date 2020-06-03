#!/usr/bin/python3
"""YET ANOTHER WILD DOCSTRING APPEARS"""


def class_to_json(obj):
    """
    ---------------------
    METHOD: CLASS TO JSON
    ---------------------
    Descriptions:
        Returns dictionary method of a given class
    Args:
        @obj: a class imported from main
    """
    # Returns the dictionary section of the class object
    # since the __dict__ sections always hold the attributes
    return obj.__dict__
