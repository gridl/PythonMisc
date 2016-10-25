# tuples are defined as:
t = (7,11,"cat", [1,1,3,5,8])
print(t)
t = 7,
print(t, len(t))

# assgining individual variables
t = 7, "cat"
n = t[0]
a = t[1]

print(n)
print(a)

# unpacking
for idx, item in enumerate(['hat','cat','mat','that']):
    print("{} -> {}".format(idx,item))