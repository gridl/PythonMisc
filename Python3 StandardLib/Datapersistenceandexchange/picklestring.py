# use dumps to encode a data structure as a strung and then print the string to the console
# pickle will be written in binary by default
# after data is serialized, can be written into a file,socket,pipe etc
import pickle
import pprint

data = [{'a':'A', 'b':2, 'c':3.0}]
print('DATA:', end=' ')
pprint.pprint(data)

data_string = pickle.dumps(data)
print('PICKLE: {}'.format(data_string))

data2 = pickle.loads(data_string)
print('After: ',end=' ')
pprint.pprint(data2)

print('SAME? :', (data is data2))
print('EQUAL?:', (data == data2))

# newly constructed object is equal to but not the same object as the original

