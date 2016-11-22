def add(a,b):
    return a + b

def subtract(a,b):
    return a -b

def multiple(a,b):
    return a*b

def divide(numerator,denominator):
    return float(numerator)/denominator


import unittest

class TestAdd(unittest.TestCase):
    """ Test the add function from the mymath library"""
    def test_add_integers(self):
        """ Test that the addition of two integers return the correct total"""

        result = add(1,2)
        self.assertEqual(result, 13)


    def test_add_floats(self):
        """ Test that the addition of two floats returns the correct result"""
        result = add(10.5,2)
        self.assertEqual(result, 12.5)


    def test_add_strings(self):
        """Test the addition of two strings retrusn the two string as one concatenated string"""
        result = add('abc','def')
        self.assertEqual(result, 'abcdef')


    def test_subtract_int(self):
        result = subtract(40,3)
        self.assertEqual(result,37)

if __name__ == '__main__':
    unittest.main()

# TO run file - coverage run <filename>.py
# TO get coverage report - coverage report -m
# Missing indicates lines of code that do not have any coverage
# coverage html to get html file