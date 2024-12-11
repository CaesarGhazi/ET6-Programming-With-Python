import unittest

from ..sort_list import sort_list

class TestSortList(unittest.TestCase):
    """Test for the sorting of a list while appending another one to it """
    def test_random_input(self):
        """It should return the list in order"""
        actual = sort_list([1, 0, 4, 2, 3],) 
        expected = [0, 1, 2, 3, 4]
        self.assertEqual(actual, expected)
        
    def test_empty_input(self):
        """It should return an empty string"""
        actual = sort_list([],) 
        expected = []
        self.assertEqual(actual, expected)
        
    def test_with_negative_input(self):
        """It should return the list in order"""
        actual = sort_list([-6, -8, 5, 4, 7],) 
        expected = [-8, -6, 4, 5, 7]
        self.assertEqual(actual, expected)

