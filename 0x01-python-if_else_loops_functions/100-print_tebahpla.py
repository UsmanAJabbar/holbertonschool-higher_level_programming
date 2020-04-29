#!/usr/bin/python3

tick = 0
# Iterate the amount of letters
for alphabets in range(122, 96, -1):
    if tick == 1:
        tick = 0
        alpha = -32
    else:
        tick = 1
        alpha = 0
    # switch stores the captial/lower
    switch = alphabets + alpha
    print("{:c}".format(switch), end='')
print("")
