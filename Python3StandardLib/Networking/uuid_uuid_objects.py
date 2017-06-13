
# Versions 3 and 5 of the UUID specifications use cryptographic hash values(MD5 or SHA-1 respectively) to combine namespace-specific seed values with names

import uuid
#UUID
hostnames = ['www.pythonanywhere.com','www.python.com']

for name in hostnames:
    print('name')
    print('MD5 ', uuid.uuid3(uuid.NAMESPACE_DNS, name))
    print('SHA-1 ',uuid.uuid5(uuid.NAMESPACE_DNS, name))
    print()


# parse strings in standard formats to crate UUID projects, making it easier to handle comparisons and sorting operations

def show(msg, l):
    print(msg)
    for v in l:
        print(' ',v)
    print()

input_values = [
    'urn:uuid:f2f84497-b3bf-493a-bba9-7c68e6def80b',
    '{417a5ebb-01f7-4ed5-aeac-3d56cd5037b0}',
    '2115773a-5bf1-11dd-ab48-001ec200d9e0',
]

show('input_values', input_values)

uuids = [uuid.UUID(s) for s in input_values]
show("converted to uuids", uuids)

uuids.sort()
show('sorted ', uuids)