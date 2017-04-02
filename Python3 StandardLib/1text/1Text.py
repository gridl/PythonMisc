import string

a = "This is a test string"
#print(a)
#print(string.capwords(a))

# Template varaibles are identified by prefixing the name with $

values = {'var':'foo'}

t = string.Template("""
Variable        : $var
Escape          : $$
Variable in text: ${var}iable
""")

print('Template:', t.substitute(values))


t = string.Template("$var is here but $missing is not provided")

try:
    print('substitute() :', t.substitute(values))
except KeyError as Err:
    print('Error:',str(Err))


print('safe_substitute():', t.safe_substitute(values))

