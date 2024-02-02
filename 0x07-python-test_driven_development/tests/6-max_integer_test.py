#!/usr/bin/python3
"""Max integer - Unittest"""
import unittest


def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result


class Max_integer_test(unittest.TestCase):
    """max int tests"""

    def test_list_of_int(self):
        """tests a lsit of integers"""
        self.assertEqual(20, max_integer([1, 9, 2, 14, 20]))

    def test_empty_list(self):
        """test for empty list"""
        self.assertIsNone(max_integer([]))

    def test_all_equal(self):
        self.assertEqual(20, max_integer([20, 20, 20, 20]))

    def test_zero_integers(self):
        """list of zeros"""
        self.assertEqual(0, max_integer([0, 0, 0, 0]))

    def test_negative_numbers(self):
        """list of negative numbers"""
        self.assertEqual(-9, max_integer([-20, -33, -9, -19]))

    def test_neg_nd_positive_numbers(self):
        """list of positive and negative numbers"""
        self.assertEqual(20, max_integer([-20, 12, 17, -19, 20]))

    def test_mixed_types(self):
        """list of mixed types"""
        with self.assertRaises(TypeError):
            max_integer([1, 2, 'er', 50])

    def test_floats(self):
        """list of floats"""
        self.assertEqual(7.8, max_integer([3.4, 6.7, 7.8]))
