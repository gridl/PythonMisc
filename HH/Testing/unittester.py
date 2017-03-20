#UNIT TEST

import unittest

def fun(x):
    return x + 1

def sub(x):
    return x - 1

class MyTest(unittest.TestCase):
    def test_that_fun_adds_one(self):
        self.assertEqual(fun(3), 4)

class MySecondTest(unittest.TestCase):
    def  test_that_fun_fails_when_not_adding_number(self):
        self.assertRaises(TypeError, fun, "multiply six by 9")

#Fail this
class MyThirdTest(unittest.TestCase):
    def test_that_fun_subracts_one(self):
        self.assertEqual(sub(3), 2)

#python -m unittest unittester.py



