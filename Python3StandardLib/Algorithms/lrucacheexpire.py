import functools

@functools.lru_cache(maxsize=2)
def expensive(a,b):
    print('called expensive({}, {})'.format(a,b))
    return a * b

def make_call(a,b,):
    print('({}, {})'.format(a,b), end=' ')
    pre_hits = expensive.cache_info().hits
    expensive(a,b)
    post_hits = expensive.cache_info().hits
    if post_hits > pre_hits:
        print('cache hit')


print('Establish the cache')
make_call(1, 2)
make_call(2, 3)

print('\n Use cache items')
make_call(1,2)
make_call(2,3)

print('\nCompute a new value, triggering cache expiration')
make_call(3,4)

print('\nCache still contains one old item')
make_call(2,3)

print('\n Oldest item needs to be recomputed')
make_call(1,2)


# the cache size is set to 2 entries. When the third set of unique arguments (3,4) is used the oldest item in the cache is dropped and replaced with the new result.