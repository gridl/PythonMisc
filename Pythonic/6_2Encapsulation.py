class PetSnake:
    def __init__(self,name,age):
        self.__age = age
        self.__name = name
        self._protected_val = 2
        self.normal = True


    def __str__(self):
        return "Pet: {} age:{}, protection level: {}".format(self.__name, self.__age, self._protected_val)


print("Here is my pet snake")
py = PetSnake("Slide", 6)
print(py)
print(dir(py))
#py.__name = py.__name.upper()
#print("She is named {} and {} years old".format(py.__name, py.__age))

print(py._protected_val)

# This is how you do private/protected fields in python