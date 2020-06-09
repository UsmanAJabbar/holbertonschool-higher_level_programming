#!/usr/bin/python3
"""YET ANOTHER DOCSTRING"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


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

    # --------------------------------  #
    #       INITIALIZATION TESTS        #
    # --------------------------------  #
    def test_a_id_no_inputs(self):
        """
        ---------
        TEST: test_a_id_no_inputs
        ---------
        Description:
            Test creating an instance
            without any input
        """
        o1 = Base()
        self.assertEqual(o1.id, 1)

    def test_b_id_no_inputs_increment(self):
        """
        -----------------------------------
        TEST: test_b_id_no_inputs_increment
        -----------------------------------
        Description:
            Tests whether the ID is incrementing
        """
        o2 = Base()
        self.assertEqual(o2.id, 2)

    def test_c_manual_id_input(self):
        """
        ----------------------------
        TEST: test_c_manual_id_input
        ----------------------------
        Description:
            Tests whether a manual input works
        """
        o3 = Base(12)
        self.assertEqual(o3.id, 12)

    def test_d_no_input_increment_continued(self):
        """
        -----------------------------------------
        TEST: test_d_no_input_increment_continued
        -----------------------------------------
        Description:
            Tests whether ID continues incrementing
            normally after assigning a manual ID
        """
        o4 = Base()
        self.assertEqual(o4.id, 3)

    def test_e_class_docstring_check(self):
        """
        -----------------------
        METHOD: test_e_class_docstring_check
        -----------------------
        Description:
            Tests whether a class has a docstring.
        """
        o1 = len(Base().__doc__)
        self.assertTrue(o1 > 0, True)

    def test_f_init_docstring(self):
        """
        -----------------------------
        METHOD: test_f_init_docstring
        -----------------------------
        Description:
            Tests whether the init function has a
            docstring.
        """
        o2 = len(Base().__init__.__doc__)
        self.assertTrue(o2 > 0, True)

    def test_g_to_json_string_docstring(self):
        """
        ---------------------------------------
        METHOD: test_g_from_json_string_doctest
        ---------------------------------------
        Description:
            Tests whether to_json_string
            function has a docstring.
        """
        o3 = len(Base().to_json_string.__doc__)
        self.assertTrue(o3 > 0, True)

    def test_h_save_to_file_docstring(self):
        """
        -------------------------------------
        METHOD: test_h_save_to_file_docstring
        -------------------------------------
        Description:
            Tests whether the save_to_file
            function has a docstring.
        """
        o4 = len(Base().save_to_file.__doc__)
        self.assertTrue(o4 > 0, True)

    def test_i_from_json_string_docstring(self):
        """
        -----------------------------------------
        METHOD: test_i_from_json_string_docstring
        -----------------------------------------
        Description:
            Tests whether the from_json_string
            function has a docstring.
        """
        o5 = len(Base().from_json_string.__doc__)
        self.assertTrue(o5 > 0, True)

    def test_j_create_docstring(self):
        """
        -------------------------------
        METHOD: test_j_create_docstring
        -------------------------------
        Description:
            Tests whether the create function
            has a docstring.
        """
        o6 = len(Base().create.__doc__)
        self.assertTrue(o6 > 0, True)

    def test_k_load_from_file_docstring(self):
        """
        ---------------------------------------
        METHOD: test_k_load_from_file_docstring
        ---------------------------------------
        Description:
            Tests whether the test_k_load_from_file_docstring
            has a docstring.
        """
        o7 = len(Base().load_from_file.__doc__)
        self.assertTrue(o7 > 0, True)

    def test_l_save_to_file_csv_docstring(self):
        """
        -----------------------------------------
        METHOD: test_l_save_to_file_csv_docstring
        -----------------------------------------
        Description:
            Tests whether the save_to_file_csv
            function has a docstring.
        """
        o8 = len(Base().save_to_file_csv.__doc__)
        self.assertTrue(o8 > 0, True)

    def test_m_load_from_file_csv_docstring(self):
        """
        -------------------------------------------
        METHOD: test_m_load_from_file_csv_docstring
        -------------------------------------------
        Description:
            Tests out whether the load_from_file_csv
            function has a docstring
        """
        o9 = len(Base().load_from_file_csv.__doc__)
        self.assertTrue(o9 > 0, True)

    def test_n_manual_id_str_input(self):
        """
        ----------------------------------
        METHOD: test_n_manual_id_str_input
        ----------------------------------
        Description:
            Tests whether the ID takes in a
            string.
        """
        o1 = Base("YEET")
        self.assertEqual(o1.id, "YEET")

    def test_n_manual_id_float_input(self):
        """
        ------------------------------------
        METHOD: test_n_manual_id_float_input
        ------------------------------------
        Description:
            Tests whether the ID takes in a
            float
        """
        o2 = Base(2.76)
        self.assertEqual(o2.id, 2.76)

    def test_n_manual_id_inf_float_input(self):
        """
        ----------------------------------------
        METHOD: test_n_manual_id_inf_float_input
        ----------------------------------------
        Description:
            Tests whether the id takes in an inf
            float.
        """
        o3 = Base(float('inf'))
        self.assertEqual(o3.id, float('inf'))

    def test_n_manual_id_list_input(self):
        """
        -----------------------------------
        METHOD: test_n_manual_id_list_input
        -----------------------------------
        Description:
            Tests whether the ID takes in a list.
        """
        o4 = Base([1, 2, 3])
        self.assertEqual(o4.id, [1, 2, 3])

    def test_n_manual_id_tuple_input(self):
        """
        ------------------------------------
        METHOD: test_n_manual_id_tuple_input
        ------------------------------------
        Description:
            Tests whether the ID takes in a
            tuple.
        """
        o5 = Base(("apple", "bananas"))
        self.assertEqual(o5.id, ("apple", "bananas"))

    def test_n_manual_id_boolean_input(self):
        """
        --------------------------------------
        METHOD: test_n_manual_id_boolean_input
        --------------------------------------
        Description:
            Tests whether the ID takes in a boolean
        """
        o6 = Base(False)
        self.assertEqual(o6.id, False)

    # --------------------------------  #
    #       CLASS METHOD TESTS          #
    # --------------------------------  #
    def test_o_to_json_string_badinput(self):
        """
        --------------------------------------
        METHOD: test_o_to_json_string_badinput
        --------------------------------------
        Description:
            Tests whether or not the to_json_string
            method returns None on bad input
        """
        o7 = Rectangle(2, 3, 4, 5)
        returns = o7.to_json_string([])
        self.assertEqual(returns, '[]')

    def test_o_to_json_string_goodinput(self):
        """
        ---------------------------------------
        METHOD: test_o_to_json_string_goodinput
        ---------------------------------------
        Description:
            Tests what the output from the "to
            json string" function looks like.
        """
        o8 = Rectangle(10, 7, 2, 8, 255)
        o8_actual_dict = o8.to_dictionary()
        actual_output = Base.to_json_string([o8_actual_dict])
        actual_output = Base.from_json_string(actual_output)
        exp_out = [{'x': 2, 'width': 10, 'id': 255, 'height': 7, 'y': 8}]
        self.assertEqual(exp_out, actual_output)

    def test_p_create_good_input(self):
        """
        -------------------------------
        METHOD: test_p_create_bad_input
        -------------------------------
        Description:
            Tries giving create bad inputs
        """
        o9 = Rectangle(3, 5, 1)
        o9_dictionary = o9.to_dictionary()
        o10 = Rectangle.create(**o9_dictionary)
        self.assertEqual(o10.to_dictionary(), o9_dictionary)

if __name__ == "__main__":
    unittest.main()
