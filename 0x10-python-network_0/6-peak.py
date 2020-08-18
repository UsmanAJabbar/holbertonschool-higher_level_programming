#!/usr/bin/python3
"""FINDS THE PEAK IN A LIST"""


def find_peak(list_of_integers):
    """
    -----------------
    METHOD: FIND_PEAK
    -----------------
    Description:
        Find the peak in a list of integers
    Args:
        List with integers exclusively.
    """
    in = list_of_integers
    return in if len(in) == 0 else max(in)
