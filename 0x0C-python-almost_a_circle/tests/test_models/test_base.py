#!/usr/bin/python3
"""YET ANOTHER DOCSTRING"""
import unittest


class TestCases(unittest.TestCase):
    """
    -----------------
    CLASS: TEST CASES
    -----------------
    Description:
        A ton of asserting.
    Notes:
        I hate it.
    Args:
        Nil.
    """

    def test_good_input(self):
        """
        -----------------------
        METHOD: TEST GOOD INPUT
        -----------------------
        """
        
        
From the base class, we need to test:
Test if the base class exists
Test if the base class gets good input, if no input, class must be initialized
    else, anything but an int must raise an error
Test if the base class has its id incrementing every single time
Try incrementing in the middle, before and after each class creation
Check the docstrings in the file and the class

# Base() x2, x3 <- Base(12), = 4
