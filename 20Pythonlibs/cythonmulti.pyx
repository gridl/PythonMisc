# cython: boundcheck=False, cdivision=True

import array
import threading

# thread objects want a target function to execute so we wrap our calculation inside a function
# we declare with nogil keyword that our function may want to release the gil
cpdef void target(double[:] piece) nogil:
    cdef int i,n = piece.shape[0]
    with nogil: #actual point where gil is released
        for i in range(n):
            piece[i] = i % 3

cdef int n = int(1e8)
cdef object a = array.array('d',[0,0]) * n

view = memoryview(a) # memory view of the data inside an array
piece_size = int(n/2) # split data into two parts

thread1 = threading.Thread(target=target, args = (view[:piece_size],))
thread2 = threading.Thread(target=target,args=(view[piece_size:],))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(a[:5])

#run it
# cythonize -b -i -a cythonmulti.pyx”

#(py3t) bash-3.2$ time python -c "import cythonmulti"
#array('d', [0.0, 1.0, 2.0, 0.0, 1.0])

#real    0m1.278s
#user    0m0.787s
#sys     0m0.473s
