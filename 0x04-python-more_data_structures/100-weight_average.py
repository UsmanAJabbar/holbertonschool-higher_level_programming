#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    div = 0
    mulsum = 0

    # This multiplies all of the the tuples and returns a list of
    # the individual results
    for members in my_list:
        mul = list(map(lambda members: members[0] * members[1], my_list))
        # [(1, 2), (2, 1), (3, 10), (4, 2)]
        # Stores
        # [2, 2, 30, 8]

    # We now need to add all of the elements in mul
    for elements in mul:
        mulsum = mulsum + elements
        # Generates the addition of all elements in mul
        # 42

    # This generates the weight for mul to be divided with
    for add in my_list:
        div += add[1]
        # Adds all the second members of the tuple
        # [(1, 2), (2, 1), (3, 10), (4, 2)]
        # (2 + 1 + 10 + 2)

    result = mulsum / div
    return result
