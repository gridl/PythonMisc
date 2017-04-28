import re

# Precompile the patterns

regexes = [
    re.compile(p)
    for p in ['this','that']

    ]

text = ' Does this text match the pattern?'

print('Text: {!r}\n'.format(text))

for regex in regexes:
    print('Seeking "{}" ->'.format(regex.pattern),end=' ')

    if regex.search(text):
        print('match!')
    else:
        print('no match')


        # module level functions maintain a cache of compiled expressions but teh size of the cache is limited
        # using compiled expressions directly avoids the cache lookup overhead.