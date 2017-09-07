import itertools


def smile(l):
    # create a list and flatten the list
    return list(itertools.chain(*[['o']*i for i in l]))

print(smile([1,2]))

assert(smile([]) ==[])
assert(smile([1]) == ['o'])
assert(smile([1,0,2]) == ['o','o','o'])
print('Done')