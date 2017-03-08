# accessing dictionaries
d = {'hello':'world'}
print(d.get('hello','default_value'))
print(d.get('howdy','default_value'))

if 'hello' in d:
    print(d['hello'])

#list comprehensions
a = [3,4,5]
b = [i for i in a if i >4]
print(b)

b = filter(lambda x: x> 4, a)
c = [i for i in b]
print(c)

# add three to all list members
a = [3,4,5]
b = [i + 3 for i in a]
print(b)

a = map(lambda i:i + 3, a)
b = [ c for c in a]
print(b)

#unpacking
filename, ext = "mydocument.txt".rsplit(".", 1)
print(filename, " is a ", ext, "file.")

a, *rest = [1,2,3]
print(rest)

four_nones = [None] * 4
print(four_nones)

#Join strings
letters = ['s','p','a','m']
word = ''.join(letters)
print(word)

x = list(('foo', 'foo', 'bar', 'baz'))
y = set(('foo', 'foo', 'bar', 'baz'))

print(x)
print(y)


#Exception safe contexts
import threading
some_lock = threading.Lock()
with some_lock:
    print("Test text")