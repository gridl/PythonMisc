import re
text = 'aabcdfghijk'
parser = re.search('a[b-f]*f', text)

# *f means it needs to end with an f

# * matches zero or more times
# + requires atleast once occurrence of the caraccter it is looking for
#  ? will match either once or zero times "co-?op would match both coop and co-op
# {a,b} there muse be atleast a repetitions and at most b
# xb{1,4}z xbz,xbbz,xbbbz but not xz
# ^ will attempt to amtch characters not listed inside our class [^a] will match any character except a
print(parser.group())


text = "The ants go marching one by one"
strings = ['the','one']

for string in strings:
    match = re.search(string,text)
    if match:
        print('Found "{}" in "{}"'.format(string,text))
        text_pos = match.span()
        print('test pos is ', text_pos)
        # span gives us the beginning and ending postions of the string that amtched
        print(text[match.start():match.end()])
    else:
        print('Did not find "{}"'.format(string))

# d matches digit
# D matches non-digit
# s matches whitespace
# S matches non whitespace
# w matches alphanumeric
# W matches non alphanumeric