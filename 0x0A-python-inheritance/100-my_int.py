#!/usr/bin/python3
"""THE REBEL"""


class MyInt(int):
    """
    ------------
    CLASS: MyInt
    ------------
    """

    def __eq__(self, other):
        """The not equal rebel"""
        return not int(self)

    def __ne__(self, other):
        """The equal rebel"""
        return int(self) == int(self)
