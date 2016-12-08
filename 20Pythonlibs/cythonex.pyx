import array

cdef int n = int(1e8) # variable for the datasize n now gets  a specific datatype
cdef object a = array.array('d', [0.0]) *  n
cdef double[:] mv = a # Create a memory view of the data inside the array a. Allows cython to generate code to access data inside the array.
cdef int i
for i in range(n):
    # manipulate elements of the memory view
    mv[i] = i % 3
print(a[:5])

# TO run this:
# “cythonize -b -i cythonex.pyx

# time python -c "import cythonex"

