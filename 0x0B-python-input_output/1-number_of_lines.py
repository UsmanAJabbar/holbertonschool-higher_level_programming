#!/usr/bin/python3
"""PETITION TO REMOVE THIS DOCSTRING"""


def number_of_lines(filename=""):
    """
    -----------------------
    METHOD: NUMBER OF LINES
    -----------------------
    Description:
        Returns the number of lines found in
        a given file
    Args:
        @filename: file input from main
    """
    with open(filename, mode="r", encoding="utf-8") as buffer:
        linecount = 0
        for strings in buffer:
            linecount += 1
    return linecount
