#!/usr/bin/python3
"""A RANDOM DOCSTRING FOLKS"""


def read_lines(filename="", nb_lines=0):
    """
    ------------------
    METHOD: READ LINES
    ------------------
    Description:
        Method that reads a certain number of
        lines from a file and prints it out
        to standard output.
    Args:
        @filename: file name
        @nb_lines: number of lines to read
    """
    with open(filename, mode="r", encoding="utf-8") as buffer:
        # If this method is called without nb_lines defined
        # print the whole buffer
        if nb_lines <= 0:
            print(buffer.read(), end="")

        else:
            linecount = 0
            for strings in buffer:
                print(strings, end="")
                linecount += 1
                if linecount > nb_lines:
                    return 0
