
import collections
Person = collections.namedtuple('Person','name age')

bob = Person(name='Bob', age=30)
print('\nRepresentation:',bob)

jane = Person(name='Jane', age=29)
print('\nField by name:',jane.name)

print('\nFields by  index')
for p in [bob,jane]:
    print('{} is {} years old'.format(*p))


# OrderedDict

print('Regular dictionary')
d = {}
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'

for k,v in d.items():
    print(k,v)

print('\nOrderedDict:')
d = collections.OrderedDict()

d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'

for k,v in d.items():
    print(k,v)

