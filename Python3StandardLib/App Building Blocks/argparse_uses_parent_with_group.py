import argparse

parser1 = argparse.ArgumentParser(add_help=False)
group = parser1.add_argument_group('authentication')

group.add_argument('--user',action="store")
group.add_argument('--password',action="store")


parser = argparse.ArgumentParser(parents=[parser1])

parser.add_argument('--local-arg',action='store_true',default=False)

print(parser.parse_args())