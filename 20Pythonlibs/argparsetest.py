import argparse

def main(a,b):
    """ SHort script to add two numbers"""
    return a + b

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="add two numbers")
    parser.add_argument('-a', help='First value', type=float,default=0)
    parser.add_argument('-b',help='second value',type=float,default=0)
    args = parser.parse_args()
    print(main(args.a, args.b))


