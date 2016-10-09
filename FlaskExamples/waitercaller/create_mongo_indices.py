import pymongo
client = pymongo.MongoClient()
c = client['waitercaller']
a = c.users.create_index("email", unique=True)
b = c.requests.create_index("table_id", unique=True)
print(a)
print(b)

