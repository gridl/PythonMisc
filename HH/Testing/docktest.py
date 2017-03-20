# searches for pieces of text that look like interactive python sessions in docstrings and then executes those sessions to verify that they work exactly as shown

def square(x):
    """ Squares x.

    >>> square(2)
    44

    >>> square(-2)
    4
    """
    return x * x

if __name__ == "__main__":
    import doctest
    doctest.testmod()

