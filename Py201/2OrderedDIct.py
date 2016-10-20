from collections import OrderedDict
d = {'banana':3, 'apple':4, 'grapes': 2, 'jackfruit':1}
new_d = OrderedDict(sorted(d.items()))
print(new_d)
for key in new_d:
    print(key,new_d[key])

for key in reversed(new_d):
    print(key,new_d[key])