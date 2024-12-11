import unittest

from ..string_length import string_length

class TestStringLength(unittest.TestCase):
    """Testing the string length function """
    def test_empty_list(self):
        """Should return None for an empty list"""
        actual = string_length([])
        expected = None
        self.assertEqual(actual,expected)

    def test_non_empty_list(self):
        """Should return the length of a non-empty list"""
        actual = string_length([1, 2, 3])
        expected = 3
        self.assertEqual(actual,expected)

    def test_empty_string(self):
        """Should return None for an empty string"""
        actual = string_length("")
        expected = None
        self.assertEqual(actual,expected)
    def test_non_empty_string(self):
        """Should return the length of a non-empty string"""
        actual = string_length("hello")
        expected = 5
        self.assertEqual(actual,expected)
