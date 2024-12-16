import unittest

from ..mystery_7 import mystery_7

class TestMystery7(unittest.TestCase):
    """ """
    def test_numbers_in_list(self):
        """Test with numbers in the list"""
        actual = mystery_7([[1, 2, 3], [4, 5, 6], [7, 8, 1]], 1) 
        expected = [[1, 2, 3], [7, 8, 1]]
        self.assertEqual(actual, expected)
    def test_empty_list(self):
        """Test with empty list"""
        actual = mystery_7([], []) 
        expected = []
        self.assertEqual(actual, expected)