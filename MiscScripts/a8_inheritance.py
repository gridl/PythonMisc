class parent(object):
    def __init__(self,value):
        self.value = value

    def spam(self):
        print('Parent.spam', self.value)

    def grok(self):
        print('Parent.grok')
        self.spam()

class Child1(parent):
    def yow(self):
        print('Child1.yow')


class Child2(parent):
    def spam(self):
        print('Child2.spam', self.value )

class Child3(parent):
    def spam(self):
        print('Child3.spam')
        super().spam() # Invokes the original spam() method






c = Child1(42)
c2 = Child2(42)
c3 = Child3(42)




p = parent(42)
print(p.value)
print(p.spam())
print(p.grok())
print(c.value)
print(c.yow())
print(c.spam())
print(c2.spam())
print(c3.spam())

