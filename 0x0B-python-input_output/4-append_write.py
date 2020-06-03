#!/usr/bin/python3
"""A RANDOM DOCSTRING APPEARS"""


def append_write(filename="", text=""):
    """
    --------------------
    METHOD: APPEND WRITE
    --------------------
    Description:
        Appends given text to a given file
    Args:
        @filename: file name to append content to
        @text: text to append to the file
    """
    with open(filename, mode="a", encoding="utf-8") as buffer:
        charcount = buffer.write(text)
    return charcount
