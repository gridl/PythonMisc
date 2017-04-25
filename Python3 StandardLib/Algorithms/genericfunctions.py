import functools

@functools.singledispatch # default implementation, if no typesspecic function found, as with the float case in this example
def myfunc(arg):
    print('default myfunc({!r})'.format(arg))

@myfunc.register(int) # register attribute of the new function serves as another decorator for registering alternative implementations
def myfunc_int(arg):
    print('myfunc_int({})'.format(arg))

@myfunc.register(list)
def myfunc_list(arg):
    print('myfunc_list()')
    for item in arg:
        print(' {}'.format(item))

myfunc('string argument')
myfunc(1)
myfunc(2.3)
myfunc(['a','b','c'])

