#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test Cases"""

    def test_module_docstring(self):
        """Module Docstring Check"""
        result = len(__import__('6-max_integer').__doc__)
        self.assertTrue(result > 0, True)

    def test_function_docstring(self):
        """Method/Function Docstring Check"""
        result = len(max_integer.__doc__)
        self.assertTrue(result > 0, True)

    def test_max_int(self):
        """Max Int Check"""
        self.assertEqual(max_integer([3, 4, 6, 12]), 12)
        self.assertEqual(max_integer([2, 2, 2, 2, 2]), 2)
        self.assertEqual(max_integer([-3, -2, -1]), -1)
        self.assertEqual(max_integer([-12345, -1]), -1)

if __name__ == '__main__':
    unittest.main()
