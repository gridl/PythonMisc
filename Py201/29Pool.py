from multiprocessing import Pool

def doubler(number):
    return number * 2

if __name__ == '__main__':
    numbers = [5,10,20]
    # we create an instance of the pool and tell it to create three worker processes
    # use the map method to map a function and iterable to each process
    pool = Pool(processes=3)
    print(pool.map(doubler,numbers))


