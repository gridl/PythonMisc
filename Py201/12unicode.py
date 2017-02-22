# python 3 defaults to the UTF-8 encoding
u = chr(40960) + 'abcd' + chr(1972)

print(u)
print(u.encode('ascii', 'ignore'))
print(u.encode('ascii','replace'))