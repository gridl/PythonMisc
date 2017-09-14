from math import sqrt
def p_pythagoras(x,y):
    return sqrt(x**2 + y**2)

print(p_pythagoras(1,1))


l_pythagoras = lambda x,y: sqrt(x**2 + y**2)
print(l_pythagoras(1,1))


# factorial

l_factorial = lambda n: 1 if n ==0 else n*l_factorial(n-1)
print(l_factorial(3))

# Inline IF expression

print((lambda gp:'good' if gp > 7 else 'sufficient' if gp >5 else 'insufficient') (8))

gender_code = 0
gender = 'female' if gender_code else 'male'
print(gender)