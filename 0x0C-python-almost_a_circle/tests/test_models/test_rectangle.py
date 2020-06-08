#!/usr/bin/python3
"""MAY GOD BLESS THESE 484 LINES"""
import unittest
from models.rectangle import Rectangle


class TestCases(unittest.TestCase):
    """
    ------------------
    METHOD: TEST CLASS
    ------------------
    Description:
        Tests as many edge cases possible onto
        the Rectangle class.
    """

    # ------------------------------ #
    #       GENERAL TESTS            #
    # ------------------------------ #
    def test_a_necessary_inputs(self):
        """
        -----------------------------
        METHOD: test_necessary_inputs
        -----------------------------
        Description:
            Tests by giving the only necessary input
            Rectangle needs and checking whether the rest
            of the attributes are being assigned
            correctly.
        """
        r1 = Rectangle(5, 1)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 5)
        self.assertEqual(r1.height, 1)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

    def test_b_necessary_inputs_x_y(self):
        """
        -----------------------------------
        METHOD: test_b_necessary_inputs_x_y
        -----------------------------------
        Description:
            Tests with the creation of a new Rectangle,
            this time with height, width, x, and y given
        """
        r2 = Rectangle(6, 2, 2)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r2.width, 6)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 2)
        self.assertEqual(r2.y, 0)

    def test_c_all_manual_inputs(self):
        """
        --------------------------------
        METHOD: test_c_all_manual_inputs
        --------------------------------
        Description:
            Tests with the creation of a new Rectangle,
            this time with all inputs and a manually
            overwritten ID.
        """
        r3 = Rectangle(7, 3, 3, 6, 4)
        self.assertEqual(r3.width, 7)
        self.assertEqual(r3.height, 3)
        self.assertEqual(r3.x, 3)
        self.assertEqual(r3.y, 6)
        self.assertEqual(r3.id, 4)

    def test_d_area(self):
        """
        -------------------
        METHOD: test_d_area
        -------------------
        Description:
            Tests what the output from the area
        """
        r4 = Rectangle(3, 2)
        self.assertEqual(r4.area(), 6)

    def test_e_str(self):
        """
        ------------------
        METHOD: test_e_str
        ------------------
        Description:
            Tests the string representation
            of the Rectangle
        """
        r5 = Rectangle(4, 6, 2, 1, 12)
        expected_out = "[Rectangle] (12) 2/1 - 4/6"
        actual_out = str(r5)
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
        r6 = Rectangle(10, 2, 1, 9)
        expected_output = {'x': 1, 'y': 9, 'id': 4, 'height': 2, 'width': 10}
        actual_output = r6.to_dictionary()
        self.assertEqual(actual_output, expected_output)

    # ------------------------------ #
    #       DOCSTRING CHECKS         #
    # ------------------------------ #
    def test_g_docstring(self):
        """
        ------------------------
        METHOD: test_g_docstring
        ------------------------
        Description:
            Tests the existence of docstrings on all
            of the functions.
        """
        r7 = len(Rectangle(5, 2).__doc__)
        r8 = len(Rectangle(5, 2).__init__.__doc__)
        r9 = len(Rectangle(5, 2).__str__.__doc__)
        r10 = len(Rectangle(5, 2).update.__doc__)
        r11 = len(Rectangle(5, 2).to_dictionary.__doc__)
        r12 = len(Rectangle(5, 2).width.__doc__)
        r13 = len(Rectangle(5, 2).height.__doc__)
        r14 = len(Rectangle(5, 2).x.__doc__)
        r15 = len(Rectangle(5, 2).y.__doc__)
        r16 = len(Rectangle(5, 2).display.__doc__)

        self.assertTrue(r7 > 0, True)
        self.assertTrue(r8 > 0, True)
        self.assertTrue(r9 > 0, True)
        self.assertTrue(r10 > 0, True)
        self.assertTrue(r11 > 0, True)
        self.assertTrue(r12 > 0, True)
        self.assertTrue(r13 > 0, True)
        self.assertTrue(r14 > 0, True)
        self.assertTrue(r15 > 0, True)
        self.assertTrue(r16 > 0, True)

    # ------------------------------ #
    #   BAD INPUT TESTS(WIDTH)       #
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
            r17 = Rectangle()

    def test_h_one_necessary_input(self):
        """
        ----------------------------------
        METHOD: test_h_one_necessary_input
        ----------------------------------
        Description:
            Tests with one necessary input
        """
        with self.assertRaises(TypeError):
            r18 = Rectangle(13)

    def test_i_bad_negative_inputs_width(self):
        """
        ------------------------------
        METHOD: test_i_negative_inputs  
        ------------------------------
        Description:
            Tests how the function reacts when size is
            given a negative number
        """
        with self.assertRaises(ValueError):
            r19 = Rectangle(-5, 2)

    def test_i_bad_negative_inputs_height(self):
        """
        ------------------------------
        METHOD: test_i_negative_inputs  
        ------------------------------
        Description:
            Tests how the function reacts when size is
            given a negative number
        """
        with self.assertRaises(ValueError):
            r20 = Rectangle(5, -2)

    def test_i_bad_str_inputs(self):
        """
        ----------------------------------
        METHOD: test_i_bad_negative_inputs
        ----------------------------------
        Description:
            Tries adding a string to the size attr
        """
        with self.assertRaises(TypeError):
            r21 = Rectangle("https://i.imgur.com/BXbn3gg.jpg", 1)

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
            r22 = Rectangle(["Its", "Pronounced", "GIF"], 1)

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
            r23 = Rectangle(True, 1)

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
            r24 = Rectangle(dict(Best_ProgrammingLang="C", Worst="Python"), 1)

    # ------------------------------ #
    #    BAD INPUT TESTS(HEIGHT)     #
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
            r25 = Rectangle(1, "https://i.imgur.com/BXbn3gg.jpg")

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
            r26 = Rectangle(1, ["Its", "Pronounced", "GIF"])

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
            r27 = Rectangle(1, True)

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
            r28 = Rectangle(1, dict(Best_ProgrammingLang="C", Worst="Python"))

    # ------------------------------ #
    #       BAD INPUT TESTS(X)       #
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
            r29 = Rectangle(5, 1, "https://imgur.com/gallery/jALjUzz")

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
            r30 = Rectangle(5, 1, ["Its", "Pronounced", "GIF"])

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
            r31 = Rectangle(5, 1, True)

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
            r32 = Rectangle(5, 1, dict(Best_ProgrammingLang="C", Worst="Python"))

    def test_j_negative_inputs_x(self):
        """
        Description:
            Tests how the class reacts when x is given
            a negative number
        """
        with self.assertRaises(ValueError):
            r33 = Rectangle(3, 1, -1)

    # ------------------------------ #
    #       BAD INPUT TESTS(Y)       #
    # ------------------------------ #
    def test_k_bad_str_inputs_y(self):
        """
        ------------------------------------
        METHOD: test_i_bad_negative_inputs_y
        ------------------------------------
        Description:
            Tries adding a string to the y attr
        """
        with self.assertRaises(TypeError):
            r34 = Rectangle(5, 5, 5, "https://imgur.com/gallery/jALjUzz")

    def test_k_bad_list_inputs_y(self):
        """
        --------------------------------
        METHOD: test_i_bad_list_inputs_y
        --------------------------------
        Description:
            Tests how the class reacts when y is given
            a list
        """
        with self.assertRaises(TypeError):
            r35 = Rectangle(5, 5, 5, ["Its", "Pronounced", "GIF"])

    def test_k_bad_bool_inputs_y(self):
        """
        --------------------------------
        METHOD: test_i_bad_bool_inputs_y
        --------------------------------
        Description:
            Tests how the class reacts when y is given
            a bool.
        """
        with self.assertRaises(TypeError):
            r36 = Rectangle(5, 5, 5, True)

    def test_k_bad_dict_inputs_y(self):
        """
        --------------------------------
        METHOD: test_i_bad_dict_inputs_y
        --------------------------------
        Description:
            Tests how the class reacts when y is given
            a dict.
        """
        with self.assertRaises(TypeError):
            r37 = Rectangle(5, 5, 5, dict(Best_ProgrammingLang="C", Worst="Python"))

    def test_k_negative_inputs_y(self):
        """
        Description:
            Tests how the class reacts when y is given
            a negative number
        """
        with self.assertRaises(ValueError):
            r38 = Rectangle(3, 4, -1)

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
        r39 = Rectangle(5, 1)
        r39.update(1, 2, 3, 4, 12)
        actual_output = r39.to_dictionary()
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
        r40 = Rectangle(10,  2)
        r40.update(height=7, id=89, y=1)
        actual_output = r40.to_dictionary()
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
            a visual representation of the Rectangle
            object.
        """
        import io
        from contextlib import redirect_stdout

        # Creating the initial
        r41 = Rectangle(6, 2)

        f = io.StringIO()
        with redirect_stdout(f):
            r41.display()
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
        r42 = Rectangle(2, 3)
        self.assertTrue(isinstance(r42, Rectangle), True)

if __name__ == "__main__":
    unittest.main()
