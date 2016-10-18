import math
def main():
    args = list()
    out_params_bad(7,args)
    print("Return values (bad) : {} & {:.2f}".format(args[0], args[1]))

    v1,v2 = out_param(7)
    print("Return values (bad) : {} & {:.2f}".format(v1,v2))

#non pythonic

def out_params_bad(base:float, args:list):
    if len(args) == 0 :
        args.append(0)
        args.append(0)


    if len(args) != 2:
        raise Exception("Need to return values")


    args[0] = base * base
    args[1] = math.sqrt(base*base*base)

#pythonic
def out_param(base:float):
    r1 = base*base
    r2= math.sqrt(base*base*base)

    return r1, r2


if __name__ == '__main__':
    main()
