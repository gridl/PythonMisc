from collections import OrderedDict, defaultdict, namedtuple
from string import ascii_lowercase

print(OrderedDict(zip(ascii_lowercase, range(4))))

# specify a default value for all new keys

d = defaultdict(list)
print(d['a'])

A = namedtuple('A', 'count enabled color')
tup = A(count=1, enabled=True, color="red")
print(tup.count)
print(tup.color)
