>>> MyList = __import__('1-my_list').MyList

>>> my_list = MyList()
>>> my_list.append(1)
>>> my_list.append(4)
>>> my_list.append(4)
>>> my_list.print_sorted()
[1, 4, 4]

>>> my_list.append(7)
>>> my_list.print_sorted()
[1, 4, 4, 7]

>>> my_list.print_sorted(2)
Traceback (most recent call last):
    ...
TypeError: print_sorted() takes 1 positional argument but 2 were given

>>> my_list.append(2)
>>> my_list.print_sorted()
[1, 2, 4, 4, 7]

>>> my_list.append(22)
>>> my_list.append(21)

>>> my_list.print_sorted()
[1, 2, 4, 4, 7, 21, 22]
