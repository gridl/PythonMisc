
import unittesting_24
import unittest

# subclass Testcase and add three tests

# each method begins with "test" becuase it  tells test runner which methods are tests

class TestAdd(unittest.TestCase):
    """ Test teh add function from the mymath libary"""

    def test_add_integers(self):
        """ Test that the addition of two integers returns the corect total"""
        result = unittesting_24.add(1,2)
        self.assertEqual(result,3)

    def test_add_floats(self):
        """test that addition of floats returns the correct result """
        result = unittesting_24.add(10.5,2)
        self.assertEqual(result, 12.5)

    def test_add_strings(self):
        """ Test the addition of two strings returns the two strings concatenated string"""
        result = unittesting_24.add('abc','def')
        self.assertEqual(result,'abcdef')

    if __name__ == '__main__':
        unittest.main()