from itertools import count, islice, cycle, repeat, accumulate, chain,zip_longest, \
    combinations, combinations_with_replacement, product
for i in count(10):
    if i > 20:
        break
    else:
        print(i)


for i in islice(count(0),5):
    print(i)

count = 0
for item in cycle('XYZ'):# cycle through series infinitely
    if count > 7:
        break
    print(item)
    count += 1

print(list(accumulate(range(10))))

#flattening lists into one using chain

#my_list = list(chain(['foo','bar'], cmd, numbers))
#print(my_list)

for item in  zip_longest('ABCD', 'xy', fillvalue='BLANK'):
    print(item)

a = list(combinations('WXYZ', 2))
print(a)

for item in combinations_with_replacement('WXYZ', 2):
    print(''.join(item))

arrays = [(-1,1), (-3,3), (-5,5)]
cp = list(product(*arrays))
print(cp)