import unittest

from ..mystery_7 import mystery_7

class TestMystery7(unittest.TestCase):
    """ """
    def test_random_input(self):
        """It should return the list in order"""
        actual = mystery_7() 
        expected = [0, 1, 2, 3, 4]
        self.assertEqual(actual, expected)