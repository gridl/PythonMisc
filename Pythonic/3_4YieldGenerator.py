def classic_fibonacci(limit):
    nums = []
    current,nxt = 0,1

    while current < limit:
        current,nxt = nxt, nxt + current
        nums.append(current)

    return nums

def generator_fibonacci():
    nums = []
    current,nxt = 0,1
    while True:
        current, nxt = nxt, nxt + current
        yield current


# gernators are composible
def  even_generator(numbers):
    for n in numbers:
        if n % 2 == 0:
            yield n

# consume both generators as a pipeline here
def even_fibonacci():
    for n in even_generator(generator_fibonacci()):
        yield n


if __name__ == '__main__':
    print("Classic")
    for m in classic_fibonacci(100):
        print(m, end=', ')

    print()

    print("generator")
    # nowhere are we storing more than 1 object at a time
    for m in generator_fibonacci():

        print(m,end=', ')
        if m > 100:
            break
    print()



    print("composed")

    for n in even_fibonacci():
        print(n,end=', ')
        if n > 100:
            break
    print()