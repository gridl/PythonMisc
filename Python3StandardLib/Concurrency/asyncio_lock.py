# although asyncio usually run as single thread process, they are still built as concurrent applications
# to support safe concurrency, includes low level primitives found in threading and multiprocessing

import asyncio
import functools

def unlock(lock):
    print('callback releasing lock')
    lock.release()


async def coro1(lock):
    print('Coro1 waiting for the lock')
    with await lock:
        print('Coro1 acquired lock')
    print('Coro1 released lock')

async def coro2(lock):
    print('Coro2 waiting for the lock')
    await lock
    try:
        print('Coro2 acquired lock')
    finally:
        print('Coro2 released lock')
        lock.release()

async def main(loop):
    # Create and acquire a shared lock
    lock = asyncio.Lock() # lock can be invoked directly using await to acquire it and calling the release method as in coro2
    print('Acquiring the lock before starting coroutines')
    await lock.acquire()
    print('lock acquired: {}'.format(lock.locked()))

    # Schedule a callback to unlock the lock
    loop.call_later(0.1, functools.partial(unlock, lock))

    # Run the coroutines that want to use the lock
    print('waiting for coroutines')
    await asyncio.wait([coro1(lock), coro2(lock)])

event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop))
finally:
    event_loop.close()


