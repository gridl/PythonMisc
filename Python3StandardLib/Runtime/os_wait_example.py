import os
import sys
import time

# when starting several processes to run separate tasks, master will need to wait for one or more of then to finish starting new ones to avoid overloading the server
# when it does not matter which child process might exit first, use wait()
# it returns as soon as any child process exits()


for i in range(2):
    print('PARENT {}: FORKING {}'.format(os.getpid(),i))
    worker_pid = os.fork()
    if not worker_pid:
        print('WORKER {}: Starting '.format(i))
        time.sleep(2 + i)
        print('WORKER {}: Finishing'.format(i))
        sys.exit(i)

for i in range(2):
    print('PARENT: Waiting for {}'.format(i))
    done = os.wait()
    print('PARENT: Child done:', done)
