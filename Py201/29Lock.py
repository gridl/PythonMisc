from multiprocessing import Process, Lock

def printer(item,lock):
    """ Prints out the item that was passed in """

    lock.acquire()
    print('process')
    try:
        print(item)

    finally:
        lock.release()

if __name__ == '__main__':
    lock = Lock()
    items = ['tango', 'foxtrot', 10]
    # Loop over list and create a process for each item. Next process in line will wait for the lock to release before proceeding
    for item in items:
        p = Process(target=printer, args=(item,lock))
        p.start()

