#!/usr/bin/python3
"""OPEN FILE"""


def read_file(filename=""):
    """
    -----------------
    METHOD: READ FILE
    -----------------
    Description:
        Prints the contents of a given file.
    Args:
        @filename: file from main
    """
    # Open opens the given file in read mode, read then copies it
    # and then the print function allows us to print the contents.
    with open(filename, mode="r", encoding="utf-8") as buffer:
        print(buffer.read(), end="")
