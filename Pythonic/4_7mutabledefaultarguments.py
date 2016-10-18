def add_items_bad(name, times=1, lst=[]):
    for _ in range(0,times):
        lst.append(name)
    return lst


def add_items_good(name,times=1,lst=None):
    if lst is None:
        lst = []
    for _ in range(0, times):
        lst.append(name)
    return lst


#list_1 = add_items_bad("a", 3) # list-1 = [A,A,A]

#add_items_bad("b",2,list_1) # LIST_1 = [A,A,A,B,B]

def main():
    a = add_items_bad("a", 3)
    print(a)
    add_items_bad("b",2,a)
    print(a)

    #danger revealed here
    d = add_items_bad("d", 4)
    print(d)
    # this is now printing ['a', 'a', 'a', 'b', 'b', 'd', 'd', 'd', 'd']
    # check the pointers of a and
    print(id(a),id(d), id(a)==id(d))
    #
    print(id(a),id(d))
    print("try again")
    a = add_items_good("a", 3)
    print(a)
    add_items_good("b",2,a)
    print(a)

    #danger revelaed here

    d = add_items_good("d", 4)
    print(d)
    #
    # print(id(a), id(d))

if __name__ == '__main__':
    main()