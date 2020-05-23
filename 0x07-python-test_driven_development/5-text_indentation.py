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

    if type(text) is not str:
        raise TypeError("text must be a string")

    breakcharacters = [".", "?", ":"]
    bigtext = ""

    # MODIFY THE ORIGINAL STRING
    text = list(text)
    for indexes in range(len(text)):
        if text[indexes] in breakcharacters:
            text[indexes + 1] = '\n\n'


    # ADD MODIFIED TEXT TO BUFF
    for indexes in range(len(text)):
        bigtext += text[indexes]

    print(bigtext, end="")
