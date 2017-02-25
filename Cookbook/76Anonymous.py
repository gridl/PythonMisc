add = lambda x,y: x + y
print(add(2,3))

names = ['DB','BJ''RH','NB']
print(sorted(names, key = lambda name: name.split()[-1].lower()))


funcs = [lambda x:x+n for n in range(5)]
for f in funcs:
    print(f(0))