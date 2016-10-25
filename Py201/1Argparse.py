import argparse

def get_args():
    parser = argparse.ArgumentParser("A sample argument parser",
    epilog= "Example usage")

    # required argument
    parser.add_argument('-x', action="store", required=True, help='Help text for option X')

    # optional arguments
    parser.add_argument('-y', help="Help text for option Y", default=False)
    parser.add_argument('-z', help="Help text for Option Z", type=int)
    print(parser.parse_args())


# mutually exclusive group function
def get_args2():
    parser = argparse.ArgumentParser("A sample argument parser",
    epilog= "Example usage")

    group = parser.add_mutually_exclusive_group()
    group.add_argument('-x', '--execute', action="store", help='Help text for option Y', default=False)
    group.add_argument('-y',help='Help text for option Y', default=False)
    parser.add_argument('-z',help="help text for option Z", type=int)
    print(parser.parse_args())


if __name__ == '__main__':
    get_args2()