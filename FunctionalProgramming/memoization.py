# improve peformance


def prime(n):
    for i in range(n,0,-1):
        if all([i // x != i /x for x in range(i-1,1,-1)]):
            return i

print(prime(100000))


# caching
# memoization implemented inside the function

cache = {}

def cache_prime(n):
    if n in cache:
        return cache[n]
    for i in range(n,0,-1):
        if all([i// x!= i/x for x in range(i-1,1,-1)]):
            return i
print(cache_prime(100000))
print(cache_prime(100000))

# memoized decorator

def memoize(fnc):
    cache = {}
    def inner(*args):
        if args in cache:
            return cache[args]
        cache[args] = fnc(*args)
        return cache[args]

    return inner

@memoize
def memoized_prime(n):
    for i in range(n,0,-1):
        if all([i // x != i / x for x in range(i-1,1,-1)]):
            return i

print(memoized_prime(100000))