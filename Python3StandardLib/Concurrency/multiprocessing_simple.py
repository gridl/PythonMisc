import multiprocessing
# diide work between multiple processes based on the API for threading
# can be used instead of threading to take advantage of multiple cores to avoid computation bottlenecks associated with GIL


def worker(num):
    """ worker function"""
    print('Worker', num)

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args = (i,))
        jobs.append(p)
        p.start()




