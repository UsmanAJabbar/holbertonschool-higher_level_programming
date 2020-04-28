#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
if number < 0:
    mnumber = number * -1
else:
    mnumber = number
ld = mnumber % 10
firsthalf = "Last digit of {:d} is {:d}"

if ld > 5:
    condition = " and is greater than 5"
elif ld == 0:
    condition = " and is 0"
elif ld < 6:
    condition = " and is less than 6 and not 0"

print(firsthalf.format(number, ld) + condition)
