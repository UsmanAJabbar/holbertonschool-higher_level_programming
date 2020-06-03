#!/usr/bin/python3
"""A Random Class, Move On"""


class MyList(list):
    """"
    ----------
    METHOD: LITERALLY DOES NOTHING
    ----------
    Description:
        To be argued.
    Args:
        @list: list from main
    """""

    def print_sorted(self):
        """
        --------------------
        METHOD: PRINT_SORTED
        --------------------
        Description:
            Prints out a list sorted in ascending order.
        Args:
            @self: inherits the input from self
        """
        copy = self[:]
        print(sorted(copy))
