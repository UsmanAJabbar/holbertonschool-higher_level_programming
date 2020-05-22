#!/usr/bin/python3
"""TEXT INDENTATION"""


def text_indentation(text):
    """
    ------------------------
    METHOD: TEXT INDENTATION
    ------------------------
    Description:
        Takes in text, and pushes
        text down by two lines whenever
        a @breakcharacter is found
    Exceptions:
        If input is not a string,
        TypeError is raised
    Args:
        @text: Text input from main
    """
    breakcharacters = [".", "?", ":"]

    if type(text) is not str:
        raise TypeError("text must be a string")

    flag = 0

    for indexes in range(len(text)):
        if text[indexes] in breakcharacters:
            print(text[indexes + flag])
            if indexes < len(text):
                flag += 1
            continue
        print(text[indexes], end="")
