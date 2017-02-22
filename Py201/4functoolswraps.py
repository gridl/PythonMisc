# use wraps as a decorator to fix docstrings and names of decorated functions

# def another_function(func): # a function that accepts another function
#     def wrapper(): # a wrapping function
#         val = "THe result of %s is %s" % (func(), eval(func()))
#         return val
#     return wrapper
#
# @another_function
# def a_function():
#     # a pretty uselesss function
#     return "1+1"
#
# if __name__ == "__main__":
#     # check a function name and docstring by printing them out using
#     # the functions name and doc properties
#     print(a_function.__name__)
#     print(a_function.__doc__)

# we decorate the function called a_function with another_function
# in case above decorator is changing the decorated functions name
# and docstring to its own

from functools import wraps
def another_function(func):
    # a function that accepts another function
    @wraps(func)
    def wrapper():
        # a wrapping function
        val = "The result of %s is %s" % (func(), eval(func()))
        return val
    return wrapper

@another_function
def a_function():
    """a pretty useless function"""
    return "1 + 1"

if __name__ == "__main__":
    print(a_function.__name__)
    print(a_function.__doc__)
