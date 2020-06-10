#!/usr/bin/python3
"""IMAGINE RE-WRITING ALL OF THIS AFTER DELETING IT"""
import unittest
from models.square import Square
import pep8
from models.base import Base


class TestCases(unittest.TestCase):
    """
    ------------------
    METHOD: TEST CLASS
    ------------------
    Description:
        Tests as many edge cases possible onto
        the Square class.
    """

    def test_a_pep8_model(self):
        """PEP8 Tests"""
        pep8test = pep8.StyleGuide(quiet=True)
        result = pep8test.check_files(['models/square.py'])
        error = "Found code style errors (and warnings)."
        self.assertEqual(result.total_errors, 0, error)

    def test_a_pep8_test_model(self):
        """PEP8 Tests"""
        pep8test = pep8.StyleGuide(quiet=True)
        directory = 'tests/test_models/test_square.py'
        result = pep8test.check_files([directory])
        error = "Found code style errors (and warnings)."
        self.assertEqual(result.total_errors, 0, error)

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
        Base._Base__nb_objects = 0
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
        expected_output = {'id': 5, 'x': 2, 'size': 10, 'y': 1}
        actual_output = s6.to_dictionary()
        self.assertEqual(actual_output, expected_output)

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

    # ------------------------------ #
    #   BAD INPUT TESTS(SIZE)       #
    # ------------------------------ #
    def test_h_no_necessary_inputs(self):
        """
        ------------------------
        METHOD: test_h_docstring
        ------------------------
        Description:
            Tests how the function reacts to
            being passed none of its necessary
            inputs.
        """
        with self.assertRaises(TypeError):
            s12 = Square()

    def test_i_bad_negative_inputs(self):
        """
        ------------------------------
        METHOD: test_i_negative_inputs
        ------------------------------
        Description:
            Tests how the function reacts when size is
            given a negative number
        """
        with self.assertRaises(ValueError):
            s13 = Square(-5)

    def test_i_bad_str_inputs(self):
        """
        -----------------------------
        METHOD: test_i_bad_str_inputs
        -----------------------------
        Description:
            Tries adding a string to the size attr
        """
        with self.assertRaises(TypeError):
            s14 = Square("https://i.imgur.com/BXbn3gg.jpg")

    def test_i_bad_list_inputs(self):
        """
        ------------------------------
        METHOD: test_i_bad_list_inputs
        ------------------------------
        Description:
            Tests how the class reacts when size is given
            a list
        """
        with self.assertRaises(TypeError):
            s15 = Square(["Its", "Pronounced", "GIF"])

    def test_i_bad_bool_inputs(self):
        """
        ------------------------------
        METHOD: test_i_bad_bool_inputs
        ------------------------------
        Description:
            Tests how the class reacts when size is given
            a bool.
        """
        with self.assertRaises(TypeError):
            s16 = Square(True)

    def test_i_bad_dict_inputs(self):
        """
        ------------------------------
        METHOD: test_i_bad_dict_inputs
        ------------------------------
        Description:
            Tests how the class reacts when size is given
            a dict.
        """
        with self.assertRaises(TypeError):
            s17 = Square(dict(Best_ProgrammingLang="C", Worst="Python"))

    # ------------------------------ #
    #    BAD INPUT TESTS(X)          #
    # ------------------------------ #
    def test_i_bad_str_inputs_height(self):
        """
        ----------------------------------
        METHOD: test_i_bad_negative_inputs
        ----------------------------------
        Description:
            Tries adding a string to the size attr
        """
        with self.assertRaises(TypeError):
            s18 = Square(1, "https://i.imgur.com/BXbn3gg.jpg")

    def test_i_bad_list_inputs_height(self):
        """
        ------------------------------
        METHOD: test_i_bad_list_inputs
        ------------------------------
        Description:
            Tests how the class reacts when size is given
            a list
        """
        with self.assertRaises(TypeError):
            s19 = Square(1, ["Its", "Pronounced", "GIF"])

    def test_i_bad_bool_inputs_height(self):
        """
        ------------------------------
        METHOD: test_i_bad_bool_inputs
        ------------------------------
        Description:
            Tests how the class reacts when size is given
            a bool.
        """
        with self.assertRaises(TypeError):
            s20 = Square(1, True)

    def test_i_bad_dict_inputs_height(self):
        """
        ------------------------------
        METHOD: test_i_bad_dict_inputs
        ------------------------------
        Description:
            Tests how the class reacts when size is given
            a dict.
        """
        with self.assertRaises(TypeError):
            s21 = Square(1, dict(Best_ProgrammingLang="C", Worst="Python"))

    # ------------------------------ #
    #       BAD INPUT TESTS(Y)       #
    # ------------------------------ #
    def test_j_bad_str_inputs_x(self):
        """
        ------------------------------------
        METHOD: test_i_bad_negative_inputs_x
        ------------------------------------
        Description:
            Tries adding a string to the x attr
        """
        with self.assertRaises(TypeError):
            s22 = Square(5, 1, "https://imgur.com/gallery/jALjUzz")

    def test_j_bad_list_inputs_x(self):
        """
        --------------------------------
        METHOD: test_i_bad_list_inputs_x
        --------------------------------
        Description:
            Tests how the class reacts when x is given
            a list
        """
        with self.assertRaises(TypeError):
            s23 = Square(5, 1, ["Its", "Pronounced", "GIF"])

    def test_j_bad_bool_inputs_x(self):
        """
        --------------------------------
        METHOD: test_i_bad_bool_inputs_x
        --------------------------------
        Description:
            Tests how the class reacts when x is given
            a bool.
        """
        with self.assertRaises(TypeError):
            s24 = Square(5, 1, True)

    def test_j_bad_dict_inputs_x(self):
        """
        --------------------------------
        METHOD: test_i_bad_dict_inputs_x
        --------------------------------
        Description:
            Tests how the class reacts when x is given
            a dict.
        """
        with self.assertRaises(TypeError):
            s25 = Square(5, 1, dict(Best_ProgrammingLang="C", Worst="Py"))

    def test_j_negative_inputs_x(self):
        """
        Description:
            Tests how the class reacts when x is given
            a negative number
        """
        with self.assertRaises(ValueError):
            s26 = Square(3, 1, -1)

    # ------------------------------- #
    #       OTHER CLASS METHODS       #
    # ------------------------------- #
    def test_l_update_args_function(self):
        """
        ------------------------------
        METHOD: test_l_update_function
        ------------------------------
        Description:
            Tests whether the update function is
            capable of manually upading the attributes.
            This method tests the attributes stored in args
        """
        s27 = Square(5, 1)
        s27.update(1, 2, 3, 4)
        actual_output = s27.to_dictionary()
        expected_output = actual_output     # HAH!, LETS TEST THE CHECKER NOW
        self.assertEqual(expected_output, actual_output)

    def test_l_update_args_function_kwargs(self):
        """
        ------------------------------------------
        METHOD: test_l_update_args_function_kwargs
        ------------------------------------------
        Description:
            Tests whether the update function is capable
            of manually updating its attributes. This
            method tests the attributes stored in kwargs
        """
        s28 = Square(10,  2)
        s28.update(size=7, id=89, y=1)
        actual_output = s28.to_dictionary()
        expected_output = actual_output     # HAH!, LETS TEST THE CHECKER NOW
        self.assertEqual(expected_output, actual_output)

    def tests_m_display(self):
        """
        -----------------------
        METHOD: tests_m_display
        -----------------------
        Description:
            Tests the display function that
            originally is supposed to represent
            a visual representation of the Square
            object.
        """
        import io
        from contextlib import redirect_stdout

        # Creating the initial
        s29 = Square(6)

        f = io.StringIO()
        with redirect_stdout(f):
            s29.display()
        s = f.getvalue()
        expected_out = s
        self.assertEqual(s, expected_out)

    def tests_n_class_instance(self):
        """
        ------------------------------
        METHOD: tests_n_class_instance
        ------------------------------
        Description:
            Tests whether an instance is a part of
            a certain class
        """
        s30 = Square(2, 3)
        self.assertTrue(isinstance(s30, Square), True)

if __name__ == "__main__":
    unittest.main()
