def spam(a,b,c,d):
    print(a,b,c,d)



from functools import partial
s1 = partial(spam, 1)
s1(1,2,3,4)