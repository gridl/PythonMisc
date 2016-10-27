from itertools import count, islice, cycle, repeat, accumulate, chain
for i in count(10):
    if i > 20:
        break
    else:
        print(i)


for i in islice(count(0),5):
    print(i)

count = 0
for item in cycle('XYZ'):# cycle through series infinitely
    if count > 7:
        break
    print(item)
    count += 1

print(list(accumulate(range(10))))

#flattening lists into one using chain

my_list = list(chain(['foo','bar'], cmd, numbers))
print(my_list)