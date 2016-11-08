#Method resolution order - list of types that the class is derived from

class X:
    def __init__(self):
        print('X')
        super().__init__()

class Y:
    def __init__(self):
        print('Y')
        super().__init__()

class Z(X,Y):
    pass

z = Z()
print(Z.__mro__)
#MRO is ZXY and then the object

class Base:
    var = 5
    def __init__(self):
        pass

class X(Base):
    def __init__(self):
        print('X')
        super().__init__()

class Y(Base):
    var = 10
    # Y overrides the base class's class variable and sets it to 10
    def __init__(self):
        print('Y')
        super().__init__()

class Z(X,Y):
    pass

z = Z()
print(Z.__mro__)
print(super(Z, z).var)
