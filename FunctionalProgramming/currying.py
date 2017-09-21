# currying is a specific kind of argument binding in whihc we create a sequence of functions that each take exactly one argument

from functools import partial


def add(a,b,c,):
    return a + b + c

print(add(10,100,1000))

add_10 = partial(add, 10)
add_10_100 = partial(add_10, 100)
print(add_10_100(1000))

# Implement the same with a decorator

from inspect import signature

def curry(fnc):
    def inner(arg): # inner function
        if len(signature(fnc).parameters) ==1:
            return fnc(arg)
        return curry(partial(fnc, arg)) # recursive currying

    return inner


@curry
def add(a,b,c):
    return a + b +c

add_10 = add(10)
add_10_100 = add_10(100)
print(add_10_100(1000))
