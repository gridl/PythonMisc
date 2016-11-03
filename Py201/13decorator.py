import random
import time

def timerfunc(func):
    # a timer decorator
    def function_timer(*args, **kwargs):
        # a nested function for timing other functions
        start = time.time()
        value = func(*args, **kwargs)
        end = time.time()
        runtime = end - start
        msg = "The runtime for {func}  took {time} seconds to complete"
        print(msg.format(func=func.__name__, time=runtime))
        return value
    return function_timer

@timerfunc # decorator accepts a function and has another fucntion inside of it
def long_runner():
    for x in range(5):
        sleep_time = random.choice(range(1,5))
        time.sleep(sleep_time)

if __name__ == '__main__':
    long_runner()

# Timing context manager

class MyTimer():

    def __init__(self):
        self.start = time.time()
        # use the class's init method to start our timer

    def __enter__(self):
        return self
        # enter method doesnt need to do anything other than return itself

    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time.time()
        runtime = time.time()
        runtime = end - self.start
        msg = 'The function took {time} seconds to complete'
        print(msg.format(time=runtime))
        # exit method has all the juicy bits

def long_runner():
    for x in range(5):
        sleep_time = random.choice(range(1,5))
        time.sleep(sleep_time)

if __name__ == '__main__':
    with MyTimer():
        long_runner()