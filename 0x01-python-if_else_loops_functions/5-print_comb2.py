#!/usr/bin/python3

for numbers in range(0, 100):
    print("{:1d}".format(numbers), end='')
    if numbers < 99:
        print(", ", end='')
