class Parent(object):
    def spam(self):
        print('Parent.spam')

class A(Parent):
    def spam(self): # redefine spam function
        print('A.spam')
        super().spam() # call super to call parent

class B(A):
    def spam(self):
        print('B.spam')
        super().spam()


class C(Parent):
    def spam(self):
        print('C.spam')
        super().spam()
a = A()
a.spam()

# MRO = method resolution order

