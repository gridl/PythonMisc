import multiprocessing

# start a job in a separate process to use process and pass a target function, it is possible to use a custom subclass

class Worker(multiprocessing.Process):
    def run(self):
        print('IN {} '.format(self.name))
        return


if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = Worker()
        jobs.append(p)
        p.start()

    for j in jobs:
        j.join()