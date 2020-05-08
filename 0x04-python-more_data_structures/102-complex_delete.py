#!/usr/bin/python3
def complex_delete(a_dictionary, value):

    copied = dict(a_dictionary)
    delcount = 0  # Number of keys deleted

    # Loop through the dictionary, if value's
    # found, then delete and then continue search
    for keys, v in copied.items():
        if v == value:
            del a_dictionary[keys]
            delcount += 1

    if delcount == 0:
        return copied
    else:
        return a_dictionary
