import unittest

from ..addition import addition

class TestAddition(unittest.TestCase):
    """Testing the addition function """
    
    def test_0(self):
        """it should test the addition of 1 and 1 """
        actual = addition(1,1)
        expected = (2)
        self.assertEqual(actual,expected)
