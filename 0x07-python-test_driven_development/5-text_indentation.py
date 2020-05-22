#!/usr/bin/python3
def text_indentation(text):
    breakcharacters = [".", "?", ":"]

    if type(text) is not str:
        raise TypeError("text must be a string")

    for characters in text:
        if characters in breakcharacters:
            print(characters + "\n")
            continue
        print(characters, end="")
