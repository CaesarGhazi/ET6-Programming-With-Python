import unittest

from ..addition import addition

class TestAddition(unittest.TestCase):
    """Testing the addition function """
# TESTS SHOULD START WITH THE WORD test OR THEY WON'T WORK
    def test_add_1_1(self):
        """it should test the addition of 1 and 1 """
        actual = addition(1,1)
        expected = 2
        self.assertEqual(actual,expected)
        
    def test_add_2_1(self):
        """it should test the addition of 2 and 1 """
        actual = addition(2,1)
        expected = 2
        self.assertEqual(actual,expected)
        
    def test_add_2_3(self):
        """it should test the addition of 2 and 3 """
        actual = addition(2,3)
        expected = 5
        self.assertEqual(actual,expected)
        