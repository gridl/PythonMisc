l_factorial = lambda n : 1 if n == 0 else n*l_factorial(n-1)

def chain_mul(*what):

    total = 1
    for (fnc,arg) in what:
        total *= fnc(arg)
    return total


print(chain_mul((l_factorial, 2),(l_factorial,3)))


import operator

def chain(how, *what):
    total = 1
    for (fnc,arg) in what:
        total = how(total, fnc(arg))
    return total

chain(operator.mul,(l_factorial,2), (l_factorial,3))