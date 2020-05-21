#!/usr/bin/python3
def text_indentation(text):
    breakcharacters = [".", "?", ":"]

    if type(text) is not str:
        raise TypeError("text must be a string")

    for i in range(len(text)):
        for j in range(len(breakcharacters)):
            if breakcharacters[j] == text[i]:
                print(breakcharacters[j])
                i += 1
        print(text[i], end="")
