#!/usr/bin/python3
from sys import argv

# IMPORT GUARD
if __name__ == '__main__':
    argc = (len(argv) - 1)  # -1 to exclude the program filename count

    # argc check
    if argc <= 0:
        print("{:d} arguments.".format(argc))
    elif argc == 1:
        print("{:d} argument:".format(argc))
        print("{:d}: {}".format((argc), argv[argc]))
    elif argc >= 2:
        print("{:d} arguments:".format(argc))
        # Print all of the words ( + 1 to print exclude file name )
        for wordindex in range(argc):
            print("{:d}: {}".format((wordindex + 1), argv[wordindex + 1]))
