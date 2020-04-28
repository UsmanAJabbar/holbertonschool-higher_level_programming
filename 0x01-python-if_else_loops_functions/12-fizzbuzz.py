#!/usr/bin/python3

for sodas in range(0, 101):
    if sodas % 15 == 0:
        print("FizzBuzz", end=' ')
        continue
    elif sodas % 3 == 0:
        print("Fizz", end=' ')
    elif sodas % 5 == 0:
        print("Buzz", end=' ')
    print("{:d}".format(sodas), end=' ')
