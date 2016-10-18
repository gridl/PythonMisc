import random
letters = 'abcdefghijklmnopqrstuvwxyz1234567890'

# C style
index = random.randint(0, len(letters)-1)
item = letters[index]
print(item)

#pythonic leverage python standard library
item = random.choice(letters)
print(item)
