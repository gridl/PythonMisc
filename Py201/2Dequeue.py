# deques are thread safe and support memory efficient appends and pops from either side of the deque
#
# from collections import deque
# import string
# d = deque(string.ascii_lowercase)
# d.append('bork')
# print(d)


# same way as a linux tail program
from collections import deque

def get_last(filename, n=5):
    try:
        with open(filename) as f:
            return deque(f,n)
    except OSError:
        print("Error opening file: {}".format(filename))
        raise

print(get_last('1Argparse.py', n=15))