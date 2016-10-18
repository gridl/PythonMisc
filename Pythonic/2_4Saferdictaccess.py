from collections import defaultdict

data = {"year": 2001, "country":"USA", "title":"Johhny 5", "duration":"119 min"}

print('optimistic style')

print(data['year'])
#print(data['rating'])

print("pessimistic style")
try:
    print(data['year'])
    print(data['rating'])
except Exception as x:
    print("OOps ! {}".format(x))


print("Safesty first style")
if 'year' in data:
    print(data['year'])
if 'rating' in data:
    print(data['rating'])
else:
    print("oh we did  not find a rating")


#If willing to except none
print("Accept none instead style")
print(data.get('year'))
print(data.get('rating'))


print("explicit alternate value style")
print(data.get('year', 0))
print(data.get('rating', '***'))


# when you call defaultdict, make sure you use a [] to ensure default dict
data = defaultdict(lambda: "MISSING", data)
print("Accept default value instead style")
print(data['year'])
print(data['rating'])