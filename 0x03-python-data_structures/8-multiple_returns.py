#!/usr/bin/python3


def multiple_returns(sentence):
    if sentence:
        strlen = len(sentence)
        firstchar = sentence[0]
        return strlen, firstchar
    else:
        return None
