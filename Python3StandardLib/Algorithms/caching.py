import functools

@functools.lru_cache() # decorator wraps a function in a least-recently used cache.Arguments ot the function are used to build a hash key, whihc is then mapped to a result
def expensive(a,b): # subsequent calls with the same arguments will fetch value from the cache instead of calling the function
    # the decorator also adds methods to the function to examine the state of the cache (cache_info) and empty the cache (cache_clear)
    print('expensive({}, {})'.format(a,b))
    return a * b

MAX = 2

print('First set of calls')
for i in range(MAX):
    for j in range(MAX):
        expensive(i,j)
print(expensive.cache_info())

print('\nSecond set of calls:')
for i in range(MAX + 1):
    for j in range(MAX +1):
        expensive(i,j)
print(expensive.cache_info())


print('\nClearing cache:')
expensive.cache_clear()
print(expensive.cache_info())

print('\nThird set of calls')
for i in range(MAX):
    for j in range(MAX):
        expensive(i,j)
print(expensive.cache_info())