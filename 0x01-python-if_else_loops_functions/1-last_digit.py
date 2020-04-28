#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
ld = number % 10
firsthalf = "Last digit of {:d} is {:d}"

if ld > 5:
    condition = " and is greater than 5"
if ld == 0:
    condition = " and is 0"
if ld < 6:
    condition = " and is less than 6 and not 0"

print(firsthalf.format(number, ld) + condition)
