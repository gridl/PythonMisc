import time
l_factorial = lambda n: 1 if n==0 else n*l_factorial(n-1)


def timer(fnc, arg):
    t0 = time.time()
    fnc(arg)
    t1 = time.time()
    return t1-t0

print('Took %.5f s' % timer(l_factorial,900))

l_timestamp = lambda fnc,arg: (time.time(), fnc(arg), time.time())
print(l_timestamp)
l_diff = lambda t0,retval,t1:t1-t0
l_timer = lambda fnc,arg:l_diff(*l_timestamp(fnc,arg))
print('Took: %.5f s' % l_timer(l_factorial,900))