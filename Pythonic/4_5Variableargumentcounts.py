# def biggest(x,y):
#     if x>y:
#         return x
#     else:
#         return y



# more than 1 argument

def biggest(x,*args):
    print(type(args), args)
    big = x
    for y in args :
        if y > big:
            big = y

    return big



print(biggest(1,7,9,10, -2 ,100))