#!/usr/bin/python3
def fizzbuzz():
    for sodas in range(1, 101):
        if sodas % 15 == 0:
            print("FizzBuzz", end=' ')
        elif sodas == 100:
            print("Buzz ")
        elif sodas % 3 == 0:
            print("Fizz", end=' ')
        elif sodas % 5 == 0:
            print("Buzz", end=' ')
        else:
            print("{:d}".format(sodas), end=' ')
