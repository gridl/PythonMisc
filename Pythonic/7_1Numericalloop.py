data = [1,7,11]
for item in data:
    print("the value is {}".format(item))



for i in range(1,10):
    print(i, end=', ')

# combination of tuple and unpacking
# enumerate gives tuple
for idx,value in enumerate(data):
    print(" {} --> {}".format(idx+1,value))
