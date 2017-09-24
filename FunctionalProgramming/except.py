def add_str(s):

    try:
        return sum([int(i) for i in  s.split('+')])
    except AttributeError:
        return None

print(add_str('1+2'))

print(add_str(1+2))


# turn that into a lambda

l_add_str = lambda s: sum([int(i) for i in  s.split('+')])

print(l_add_str('1+2'))

# handling errors within lambda

def maybe(fnc):
    def inner(*args):
        for a in args:
            if isinstance(a, Exception):
                return a
        try:
            return fnc(*args)
        except Exception as e:
            return e
    return inner

safe_add_str = maybe(lambda s: sum([int(i) for i in  s.split('+')]))

print('With maybe')
print(safe_add_str('1+2'))
print(safe_add_str(1+2))