#!/usr/bin/python3
"""YET ANOTHER DOCSTRING"""
import unittest
from models.base import Base

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
        o1 = Base()
        o2 = Base()
        o3 = Base(12)
        o4 = Base()
        o5 = Base()

        self.assertEqual(o1.id, 1)
        self.assertEqual(o2.id, 2)
        self.assertEqual(o3.id, 12)
        self.assertEqual(o4.id, 3)
        self.assertEqual(o5.id, 4)

    def test_docstrings(self):
        """
        -----------------------
        METHOD: TEST DOCSTRINGS
        -----------------------
        Description:
            Tests the existence of docstrings
            on all of the functions/methods in
            the class Base.
        """
        o1 = len(Base().__doc__)
        o2 = len(Base().__init__.__doc__)
        o3 = len(Base().to_json_string.__doc__)
        o4 = len(Base().save_to_file.__doc__)
        o5 = len(Base().from_json_string.__doc__)
        o6 = len(Base().create.__doc__)
        o7 = len(Base().load_from_file.__doc__)
        o8 = len(Base().save_to_file_csv.__doc__)
        o9 = len(Base().load_from_file_csv.__doc__)

        self.assertTrue(o1 > 0, True)
        self.assertTrue(o2 > 0, True)
        self.assertTrue(o3 > 0, True)
        self.assertTrue(o4 > 0, True)
        self.assertTrue(o5 > 0, True)
        self.assertTrue(o6 > 0, True)
        self.assertTrue(o7 > 0, True)
        self.assertTrue(o8 > 0, True)
        self.assertTrue(o9 > 0, True)

    def test_updating_ids(self):
        """
        -------------------------
        METHOD: TEST UPDATING IDS
        -------------------------
        Description:
            Tests the effects of updating the
            ID attribute with difference data
            types.
        """
        o1 = Base("YEET")
        o2 = Base(2.76)
        o3 = Base([1, 2, 3])
        o4 = Base(("apple", "bananas"))
        o5 = Base(False)

# From the base class, we need to test:
# Test if the base class exists
# Test if the base class gets good input, if no input, class must be initialized
#     else, anything but an int must raise an error
# Test if the base class has its id incrementing every single time
# Try incrementing in the middle, before and after each class creation
# Check the docstrings in the file and the class
# Test docstrings on every single fucntion

if __name__ == "__main__":
    unittest.main()
