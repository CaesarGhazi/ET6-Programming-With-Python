import unittest

from ..less_or_sum import less_or_sum

class TestLessOrSum(unittest.TestCase):
    """Testing the comparison between two numbers """
    def test_first_less_than_second(self):
        """Should return the smaller number when first_number < second_number"""
        actual = less_or_sum(3, 5)
        expected = 3
        self.assertEqual(actual,expected)
    
    def test_first_greater_than_second(self):
        """Should return the smaller number when first_number > second_number"""
        actual = less_or_sum(10, 4)
        expected = 4
        self.assertEqual(actual,expected)
    
    def test_first_equal_to_second(self):
        """Should return the sum when first_number == second_number"""
        actual = less_or_sum(7, 7)
        expected = 14
        self.assertEqual(actual,expected)
    def test_floats(self):
        """Should return the smaller number"""
        actual = less_or_sum(2.4, 2.6)
        expected = 2.4
        self.assertEqual(actual,expected)