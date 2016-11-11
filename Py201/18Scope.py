# local scope
# global scope
# nonlocal scope


def my_func(a,b):
    x = 5
    print(x)

if __name__ == '__main__':
    x = 10
    my_func(1,2)
    print(x) # x inside my_func has a local function scope and overrides the x variable outside the function
