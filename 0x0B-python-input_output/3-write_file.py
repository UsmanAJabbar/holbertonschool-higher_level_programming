#!/usr/bin/python3
"""A RANDOM DOCSTRING APPEARS"""


def write_file(filename="", text=""):
    """
    ------------------
    METHOD: WRITE FILE
    ------------------
    Description:
        Writes the given text to a file
    Args:
        @filename: file name from main
        @text: text to be written to the
        new file
    """
    with open(filename, mode = "w", encoding="utf-8") as buffer:
        charcount = buffer.write(text)
    return charcount
