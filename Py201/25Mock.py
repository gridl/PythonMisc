# from unittest.mock import Mock
# my_mock = Mock()
# my_mock.__str__ = Mock(return_value='Mocking')
# print(str(my_mock))

#Mock model asserts

from unittest.mock import Mock
# create instance of the class and add a method that returns a string using the Mock class
class TestClass():
    pass

cls = TestClass()
cls.method = Mock(return_value='mocking is fun')
print(cls.method(1,2,3))

# this will assert if we call our method two or more times with the same arguments
print(cls.method.assert_called_once_with(1,2,3))


cls.other_method = Mock('Something else')
print(cls.other_method.assert_not_called())
def my_side_effect():
    print('Updating databases')

# side effect is something that happens when you run your function
def main():
    mock = Mock(side_effect=my_side_effect)
    mock()

if __name__ == '__main__':
    main()
