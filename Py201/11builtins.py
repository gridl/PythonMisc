# ANY

widget_one = ''
widget_two = ''
widget_three = 'yes'
widgets_exist = any([widget_one,widget_three, widget_two])
print(widgets_exist)

#EVAL
var = 10
source = 'var * 2'
print(eval(source))

#FILTER - take a function and an iterable and return an iterator for those elements within the iterable for whihc the passed function returns True

def less_than_ten(x):
    return x < 10

my_list = [1,2,3,10,11,12]
for item in filter(less_than_ten, my_list):
    #print(item)
    pass


# MAP takes a function and an iterable and returns an iterator that applies the function to each item in the iterable

def doubler(x):
    return x * 2

my_list = [1,2,3,4,5]
for item in map(doubler, my_list):
    print(item)

# with list comprehension
x = [doubler(x) for x in my_list]
print(x)

# Using ZIP take twp lists and turn them into a dictionary

keys = ['x', 'y','z']
values = [5,6,7]
my_dict = dict(zip(keys,values))
print(my_dict)