#!/usr/bin/python3
"""~~~~~~~~~~~~~~~"""
import unittest
from models.square import Square


class TestCases(unittest.TestCase):
    """
    ------------------
    METHOD: TEST CLASS
    ------------------
    Description:
        Tests as many edge cases possible onto
        the Square class.
    """

    def test_a_necessary_inputs(self):
        """
        -----------------------------
        METHOD: test_necessary_inputs
        -----------------------------
        Description:
            Tests by giving the only necessary input
            square needs and checking whether the rest
            of the attributes are being assigned
            correctly.
        """
        s1 = Square(5)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)

    def test_b_necessary_inputs_x_y(self):
        """
        -----------------------------------
        METHOD: test_b_necessary_inputs_x_y
        -----------------------------------
        Description:
            Tests with the creation of a new square,
            this time with size, x, and y given
        """
        s2 = Square(6, 2, 2)
        self.assertEqual(s2.id, 2)
        self.assertEqual(s2.size, 6)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 2)

    def test_c_all_manual_inputs(self):
        """
        --------------------------------
        METHOD: test_c_all_manual_inputs
        --------------------------------
        Description:
            Tests with the creation of a new square,
            this time with all inputs and a manually
            overwritten ID.
        """
        s3 = Square(7, 3, 3, 6)
        self.assertEqual(s3.size, 7)
        self.assertEqual(s3.x, 3)
        self.assertEqual(s3.y, 3)
        self.assertEqual(s3.id, 6)

    def test_d_area(self):
        """
        -------------------
        METHOD: test_d_area
        -------------------
        Description:
            Tests what the output from the area
            function is after assigning a size.
        """
        s4 = Square(3)
        self.assertEqual(s4.area(), 9)

    def test_e_str(self):
        """
        ------------------
        METHOD: test_e_str
        ------------------
        Description:
            Tests the string representation
            of the square
        """
        s5 = Square(2, 2)
        expected_out = "[Square] (4) 2/0 - 2"
        actual_out = str(s5)
        self.assertEqual(actual_out, expected_out)

    def test_f_to_dictionary(self):
        """
        ----------------------------
        METHOD: test_f_to_dictionary
        ----------------------------
        Description:
            Checks whether the to dictionary
            function properly returns a dictionary
            of keys and values
        """
        s6 = Square(10, 2, 1)
        expected_output = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        actual_output = s6.to_dictionary()
        self.assertEqual(expected_output, expected_output)

    def test_g_docstring(self):
        """
        ------------------------
        METHOD: test_g_docstring
        ------------------------
        Description:
            Tests the existence of docstrings on all
            of the functions.
        """
        s7 = len(Square(5).__doc__)
        s8 = len(Square(5).__init__.__doc__)
        s9 = len(Square(5).__str__.__doc__)
        s10 = len(Square(5).update.__doc__)
        s11 = len(Square(5).to_dictionary.__doc__)

        self.assertTrue(s7 > 0, True)
        self.assertTrue(s8 > 0, True)
        self.assertTrue(s9 > 0, True)
        self.assertTrue(s10 > 0, True)
        self.assertTrue(s11 > 0, True)

# Test no inputs
# Test one necessary input (size)
# Test all all inputs (size, x, y, id)
# Test all negative inputs
# Test giving it bad input (Raise TypeErrors)
# Test if to_dictionary is returning the right output
# Test the string method
# Test area
# Test the update function with args and kwargs

if __name__ == "__main__":
    unittest.main()
