#!/usr/bin/python3


def max_integer(my_list=[]):
    if my_list:
        bignumba = 0  # Initializes var to 0
        # Loop through all the elements
        for elements in range(len(my_list)):
            # If list's element is larger than
            # the last one, add it to our var
            if my_list[elements] > bignumba:
                bignumba = my_list[elements]

        return bignumba

    else:
        return None
