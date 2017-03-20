def foo():
    print("Inside foo")


import logging

logging.basicConfig()


def logged(func, *args, **kwargs):
    logger = logging.getLogger()

    def new_func(*args, **kwargs):
        logger.debug("calling {} with args {} and kwargs {}".format(func.__name__, args, kwargs))
        print("this is inside decorator")
        return func(*args, **kwargs)

    return new_func


@logged
def bar():
    print("I am inside bar")


logging.getLogger().setLevel(logging.DEBUG)
bar()
foo()
