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
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return False

    def __ne__(self, other):
        """The equal rebel"""
        return not self.__eq__(other)
