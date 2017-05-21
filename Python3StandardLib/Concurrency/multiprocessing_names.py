import multiprocessing
import time

# each process instance has a nme with a default value that can be changed as the process is created
# naming processes is use ful for keeping track of them, especially in application with multiple types of processes

def worker():
    name = multiprocessing.current_process().name
    print(name,'starting')
    time.sleep(2)
    print(name,'Exiting')

def my_service():
    name = multiprocessing.current_process().name
    print(name,'Starting')
    time.sleep(3)
    print(name,'Exiting')

if __name__ == '__main__':
    service = multiprocessing.Process(
        name='my_service',
              target=my_service,
    )

    worker_1 = multiprocessing.Process(
        name='worker 1',
        target= worker
    )

    worker_2 = multiprocessing.Process(
        name = 'worker 2',
        target=worker,
    )

worker_1.start()
worker_2.start()
service.start()
