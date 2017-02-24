import html

def avg(first, *rest):
    print((first + sum(rest)) / (1 + len(rest)))


# to accept any number of arguments, use an argument that starts with **

def make_element(name,value,**attrs):
    keyvals = [' %s="%s"' % item for item in attrs.items()]
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}> {value}</{name}>'.format(name=name, attrs=attr_str,value = html.escape(value))
    print(element)



avg(1,2,3,4)
make_element('item','Albatross',size='large',quantity=6)