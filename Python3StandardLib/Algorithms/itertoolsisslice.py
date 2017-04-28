from itertools import *

print('Stop at 5:')
for i in islice(range(100),5):
    print(i, end='')
print('\n')

print('Start at 5, Stop at 10:')
for i in islice(range(100), 5,10):
    print(i,end=' ')
print('\n')

print('By tens to 100:')
for i in islice(range(100),0, 100, 10):
    print(i, end=' ')
print('\n')

#tee functio retruns several independent iterators
# can be used to feed the same set of data into multiple algorithms to be processed in parallel
r = islice(count(),5)
i1,i2 = tee(r)

print('i1: ', list(i1))
print('i2: ', list(i2))

