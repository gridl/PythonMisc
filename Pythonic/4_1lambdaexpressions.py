def main():
    print("find odd numbers via method")
    for n in find_special_numbers(check_for_odd, 50):
        print(n,end=',')
    print()

    print("Find divisible  by 6 via lambda")
    check = lambda i: i %6 ==0
    for n in find_special_numbers(check, 25):
        print(n,end=',')
    print()

    print("Sorted list of words: ")
    list_of_words = ['CPython', 'read', 'improvements', 'issues', 'in','comprehensive','port','user-facing','of','other'
                     , 'for','smaller','deprecations','a','including','and','Please','many','list']

    #TODO
    #list_of_words.sort()
    list_of_words.sort(key=lambda w: w.lower())
    print(list_of_words)

    print("done")


def find_special_numbers(special_selector, limit=10):
    found = []
    n = 0
    while len(found) < limit:
        if special_selector(n):
            found.append(n)
        n += 1
    return found

def check_for_odd(n):
    return n % 2 == 1

if __name__ == '__main__':
    main()

