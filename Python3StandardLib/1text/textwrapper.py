import textwrap

sample_text = ''' The textwrap module can be used to format text for output in    situations where pretty-printing is desired. It offers    programmatic functionality similar to the paragraph wrapping    or filling features found in many text editors.    '''

print(textwrap.fill(sample_text, width=50))

# remove existing indentation

dedented_text = textwrap.dedent(sample_text).strip()
for width in [45,60]:
    print('{} Columns \n'.format(width))
    print(textwrap.fill(dedented_text,width=width))
    print()

# Truncating Long Text

original = textwrap.fill(dedented_text, width= 50)

shortened = textwrap.shorten(original, 100)
shortened_wrapped = textwrap.fill(shortened, width=50)

print(shortened)
print(shortened_wrapped)