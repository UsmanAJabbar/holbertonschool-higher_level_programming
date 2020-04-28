#!/usr/bin/python3

for letters in range(ord('a'), ord('z') + 1):
    if letters == ord('e') or letters == ord('q'):
        continue
    print("{:c}".format(letters), end='')
