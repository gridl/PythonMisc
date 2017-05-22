import multiprocessing
import sys

# use lock to avoid conflicting accesses when a single resource needs to be shared betwwen multiple processes
def worker_with(lock, stream):
    with lock:
        stream.write('Lock acquired via with\n')

def worker_no_with(lock,stream):
    lock.acquire()
    try:
        stream.write('Lock acquired directly \n')
    finally:
        lock.release()

lock = multiprocessing.Lock()
w = multiprocessing.Process(target=worker_with, args=(lock,sys.stdout),)

nw = multiprocessing.Process(target=worker_no_with, args=(lock,sys.stdout),)

w.start()
nw.start()

w.join()