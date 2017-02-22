from multiprocessing import Process, Queue

sentinel = -1
def creator(data,q):
    """ Crates data to be consumed and waits for the ocnsumer to finish processing"""
    print('Create data and put it on the queueu')
    for item in data:
        q.put(item)

def my_consumer(q):
    """ Consumes data and works on it"""
    while True:
        data = q.get()
        print('data found to be processed'.format(data))
        processed = data * 2
        print(processed)
        if data in sentinel:
            break

if __name__ == '__main__':
    q = Queue()
    data = [5,10,13,-1]
    process_one = Process(target=creator, args =(data,q))
    process_two = Process(target=my_consumer,args =(q,))
    q.close()
    q.join_thread()
    # call join on the process objects rather than the queue itself
    process_one.join()
    process_two.join()

