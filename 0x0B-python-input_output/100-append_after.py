#!/usr/bin/python3
"""DOCSTRING"""


def append_after(filename="", search_string="", new_string=""):
    """
    --------------------
    METHOD: APPEND AFTER
    --------------------
    Description:
        Appends the given text after a search string
        is found in the given file
    Args:
        @filename:
        @search_string:
        @new_string:
    """

    # Open file in read mode to pull the contents as a list
    with open(filename, "r") as buffer:
        string_list = buffer.readlines()

    file_line_num = 0   # Keep an index count to report to insert

    # Open the same file again, but in write mode to update the data
    with open(filename, "w") as output:
        for line in string_list:
            file_line_num += 1
            if search_string in line:
                string_list.insert(file_line_num, new_string)
                break
        # Write to the file
        for strings in string_list:
            output.write(strings)
