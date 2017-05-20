import random
import threading
import time
import logging

# not necessary to retain an explicit handle to all of the daemon threads in order to ensure they have completed before exiting the main process
# enumerate returns a list of active Thread instances
def worker():
    """ thread worker function"""
    pause = random.randint(1,5)/10
    logging.debug('sleeping %0.2f', pause)
    time.sleep(pause)
    logging.debug('ending')


logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',)

for i in range(3):
    t = threading.Thread(target=worker, daemon=True)
    t.start()

main_thread = threading.main_thread()
for t in threading.enumerate():
    if t is main_thread:
        continue
    logging.debug('joining %s', t.getName())
    t.join()



