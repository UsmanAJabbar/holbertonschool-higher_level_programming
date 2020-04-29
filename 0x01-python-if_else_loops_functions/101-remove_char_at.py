#!/usr/bin/python3
def remove_char_at(str, n):
    for index in range(len(str)):
        if index == n:
            continue
        print("{:c}".format(ord(str[index])), end='')
    return("")
