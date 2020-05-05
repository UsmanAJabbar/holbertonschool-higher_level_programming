#!/usr/bin/python3

# Loop through all of the
# list and save them into a variable
# that variable must be updated if
# the next item in the list is larger
# than the value in the current variable
# Then return that variable

def max_integer(my_list=[]):
    bignumba = 0

    for elements in range(len(my_list)):
        if my_list[elements] > bignumba:
            bignumba = my_list[elements]
    return bignumba
