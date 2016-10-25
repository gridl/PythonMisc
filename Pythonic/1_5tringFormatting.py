name = 'harry'
age = 43

print("hi I'm %s and age is %d" %(name,age))


#pythonic

print("Hi Im {} and im {} years old". format(name,age))
print("Hi Im {1} and im {0} years old". format(name,age))
print("Hi Im {1} and im {0} years old ,yeah {1}". format(name,age))

data = {'day': 'Saturday', 'Office': "Home Office", 'other': "UNUSED"}
print("On {day} I was working in my {other}".format(**data))


