import argparse
import hashlib
import sys

lorem = '''Lorem ipsum dolor sit amet, consectetur adipisicing
elit, sed do eiusmod tempor incididunt ut labore et dolore magna
aliqua. Ut enim ad minim veniam, quis nostrud exercitation
ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis
aute irure dolor in reprehenderit in voluptate velit esse cillum
dolore eu fugiat nulla pariatur. Excepteur sint occaecat
cupidatat non proident, sunt in culpa qui officia deserunt
mollit anim id est laborum.'''

parser = argparse.ArgumentParser('hashlib demo')
parser.add_argument('hash_name', choices=hashlib.algorithms_available,
                    help='the name of the hash algorithms to use')


parser.add_argument('data',nargs='?',default=lorem,help='the input'
                                                        'data to hash, defaults to lorem ipsum')

args = parser.parse_args()


h = hashlib.new(args.hash_name)

h.update(args.data.encode('utf-8'))
print(h.hexdigest())