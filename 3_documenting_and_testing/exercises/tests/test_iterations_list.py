import unittest

from ..iterations_list import iterations_list

class TestIterationsList(unittest.TestCase):
    """ """
    def test_random_input(self):
        """It should return the list iterated"""
        actual = iterations_list(3,2) 
        expected = [2,3,4]
        self.assertEqual(actual, expected)
        
    def test_zero_iterations(self):
        """It should return an empty list"""
        actual = iterations_list(0, 5) 
        expected = []
        self.assertEqual(actual, expected)
        
    def test_negative_start_number(self):
        """It should return the negative numbers in order"""
        actual = iterations_list(3, -3) 
        expected = [-3, -2, -1]
        self.assertEqual(actual, expected)
