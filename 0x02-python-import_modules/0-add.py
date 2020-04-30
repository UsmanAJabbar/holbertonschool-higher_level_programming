#!/usr/bin/python3
from add_0 import add
# If code is being run from the
# main logic file then execute
if __name__ == '__main__':
    a = 1
    b = 2
    calc = add(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, calc))
