import unittest

from ..sequential_list import sequential_list

class TestSequencedList(unittest.TestCase):
    """Test the sequential list function if it returns a sequential list"""

    def test_five_member_list(self):
        """It should evaluate 5 to [0, 1, 2, 3, 4]"""
        actual = sequential_list(5)
        expected = [0, 1, 2, 3, 4]
        self.assertEqual(actual, expected)
        
    def test_empty_list(self):
        """It should evaluate 1 with an empty list"""
        actual = sequential_list(0)
        expected = []
        self.assertEqual(actual, expected)
        
    def test_negative_number_list(self):
        """It should evaluate -3 with an empty list"""
        actual = sequential_list(-3)
        expected = []
        self.assertEqual(actual, expected)
