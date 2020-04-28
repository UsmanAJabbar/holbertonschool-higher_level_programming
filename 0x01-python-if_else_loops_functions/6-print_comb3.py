#!/usr/bin/python3
for elements in range(0, 100):
    fd = int(elements / 10)
    ld = int(elements % 10)
    if fd < ld and elements < 89:
        print("{:d}{:d}, ".format(fd, ld), end='')
    if elements == 89:
        print("{:d}".format(89), end='')
print("")
