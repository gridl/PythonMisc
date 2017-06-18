import argparse

parser = argparse.ArgumentParser(description='Example with long option names')

parser.add_argument('--noarg', action='store_true',default=False) # boolean option, store_true implies save the boolean value
parser.add_argument('--witharg', action='store',dest='witharg') # simple string option
parser.add_argument('--witharg2',action='store',dest='witharg2', type=int) # integer option

print(parser.parse_args(['--noarg','--witharg','val','--witharg2=3']))