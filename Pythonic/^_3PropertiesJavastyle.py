class NotSoPythonicPet:
    #def __init__(self):
    def __init__(self, name,age):
        self.age = age
        self.name = name

        #
        # def get_name(self):
        #     return self.name
        #
        #
        # def get_age(self):
        #     return self.age

# print("Here is my pet cow")
# cow = NotSoPythonicPet('betsy', 11)
# print("She is named {} and {} years old".format(cow.get_name(), cow.get_age()))
# print()


class PetSnake:
    def __init__(self,name,age) :
        self.__age = age
        self.__name = name
        self.__protected_val = 2

    @property
    def name(self):
        return self.__age
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

print("Here is my pet snake")
py = PetSnake("Slide", 6)
# cant set below attribute as its protected
#py.age = 4


print("She is named {} and {} years old ".format(py.name,py.age))

# added a new @agesetter
py.age = 4
print("She is named {} and {} years old ".format(py.name,py.age))