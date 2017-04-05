import re
text = 'abbaaaabbbbaaabbaa'
pattern = 'ab'

for match in re.findall(pattern,text):
    print('Found {!r}'.format(match))


# FInd iter returns an iterator that produces Match instances instead of the strings retruned by findall()

for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()

    print( 'Found {!r} at  {:d}:{:d}'.format(text[s:e], s,e)
    )



    test_patterns(
        'A prime #1 example!',
        [(r'\d+', 'sequence of digits'),
         (r'\D+', 'sequence of nondigits'),
         (r'\s+', 'sequence of whitespace'),
         (r'\S+', 'sequence of nonwhitespace'),
         (r'\w+', 'alphanumeric characters'),
         (r'\W+', 'nonalphanumeric')],
    )