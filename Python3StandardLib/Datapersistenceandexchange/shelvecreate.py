import shelve
import dbm
# shelve persistent storage option for python objects when a relational database is not required

with shelve.open('test_shelf.db') as s:
    s['key1'] = {
        'int': 10,
        'float': 9.5,
        'string': 'Sample data',
    }

with shelve.open('test_shelf.db') as s:
    existing = s['key1']
print(existing)

# open it as read-only

with shelve.open('test_shelf.db', flag='r') as s:
    print('Existing:', s['key1'])
    try:
        s['key1'] = 'new value'
    except dbm.error as err:
        print('ERROR: {}'.format(err))

#write-back - if the contents of an item stored i the shelf are changed, the shelf must be updated explictly by storing the entire item again

with shelve.open('test_shelf.db') as s:
    print(s['key1'])
    s['key1']['new_value'] = 'this was not here before'

with shelve.open('test_shelf.db', writeback=True) as s:
    print(s['key1'])


