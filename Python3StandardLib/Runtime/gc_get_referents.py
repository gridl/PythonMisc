import gc
import pprint

class Graph():
    def __init__(self,name):
        self.name = name
        self.next = None


    def set_next(self,next):
        print('Linking nodes {}.next = {}'.format(self,next))
        self.next = next

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__,self.name)


# construct a graph cycle
one = Graph('one')
two = Graph('two')
three = Graph('three')

one.set_next(two)
two.set_next(three)
three.set_next(one)

print()


# Remove references to the graph nodes in this module's namespace

one = two = three = None

# Show the effect of garbage collection

for i in range(2):
    print('Collecting {} ...'.format(i))
    n = gc.collect()
    print('Unreachable objects:', n)
    print('remaining garbage:', end=' ')
    pprint.pprint(gc.garbage)
