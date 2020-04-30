#!/usr/bin/python3
from sys import argv

# Import Guard
if __name__ == '__main__':
    argc = (len(argv) - 1)
    sum = 0
    # Add all of the indexes stored in argv
    for numbers in range(argc):
        sum = sum + int(argv[numbers + 1])
    # Once you're out of indexes, print sum
    print("{}".format(sum))
