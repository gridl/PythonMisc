import multiprocessing
import random
import timeit

def calculate_pi(iterations):
    x = (random.random() for i in range(iterations))
    y = (random.random() for i in range(iterations))
    r_squared = [xi**2 + yi**2 for xi,yi in zip(x,y)]
    percent_coverage = sum([r <=1 for r in r_squared]) / len(r_squared)
    return 4 * percent_coverage

def run_pool(processes, total_iterations):
    with multiprocessing.Pool(processes) as pool: # using the multiprocessing.pool within a context manager reinforces that the pool should only be used by the process that creates it
        #divide the total iterations among the processes
        iterations = [ total_iterations // processes] * processes # total iterations will alwasy be the same, they'll just be divided between a different number of processes
        result = pool.map(calculate_pi, iterations) # creates multiple processes - one per item in the iterations list

    print("%0.4f" % (sum(result) / processes), end=',  ')


ten_million = 1000000 # only one process for the first timeit trial

print(timeit.timeit(lambda: run_pool(100, ten_million), number=10))

