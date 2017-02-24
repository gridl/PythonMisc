def recv(maxsize,*,block):
    'Recieves am essage'
    pass

recv(1024,block=True)


#varying number of positional arguments

def minimum(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    print(m)

minimum(1,5,2,-5,10)
minimum(1,5,2,-5,10, clip=0)