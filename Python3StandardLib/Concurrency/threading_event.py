import logging
import threading
import time

def wait_for_event(e):
    """ wait for the evetn to be set before doing anything"""
    logging.debug('wait for event starting')
    event_is_set = e.wait()
    logging.debug('event set: %s', event_is_set)

def wait_for_event_timeout(e,t):
    """ wait t seconds then timeout """
    while not e.is_set():
        logging.debug('wait for event timout starting')
        event_is_set = e.wait(t)
        logging.debug('event set: %s', event_is_set)
        if event_is_set:
            logging.debug('processing event')
        else:
            logging.debug('doing other work')

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s) %(message)s',)

e = threading.Event()
t1 = threading.Thread(name='block',target=wait_for_event,args=(e,))
t1.start()

t2 = threading.Thread(name='nonblock',target=wait_for_event_timeout,args=(e,2),)
t2.start()

logging.debug('waiting before calling Event.set()')
time.sleep(0.3)
e.set()
logging.debug('event is set')