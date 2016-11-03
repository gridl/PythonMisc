#timeit

def my_function():
    try:
        1/0
    except ZeroDivisionError:
        pass

if __name__ == "__main__":
    import timeit
    # setup string to import the function into timeits namespace
    setup = "from __main__ import my_function"
    print(timeit.timeit("my_function()",setup=setup))


