#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer

a = Any Value
b = 98 (By Default unless mentioned)

If a is a float, then that float must be converted into an int before adding

>>> add_integer(2, 4)
6

>>> add_integer(4)
102

>>> add_integer(3.2)
101

>>> add_integer(5, 6.8)
11

>>> add_integer(5.5, 20.2)
24

>>> add_integer("Yeet")
Traceback(most recent call last):
    ...
TypeError: a must be an integer

>>> add_integer({})
Traceback(most recent call last):
    ...
TypeError: a must be an integer

>>> add_integer([])
Traceback(most recent call last):
    ...
TypeError: a must be an integer

>>> add_integer('a')
Traceback(most recent call last):
    ...
TypeError: a must be an integer

>>> add_integer(-20.5)
-20

>>> add_integer()
Traceback(most recent call last):
    ...
TypeError: add_integer() missing 1 required positional argument: 'a'