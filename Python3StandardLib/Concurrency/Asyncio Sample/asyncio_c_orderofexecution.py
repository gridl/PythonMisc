import random
from time import sleep

import asyncio

def task(pid):
    ### Synchronous nondeterminisitc task
    sleep(random.randint(0,2) * 0.001)
    print('Task %s done' % pid)

async def task_coro(pid):
    # Coroutine on-deterministic task
    await asyncio.sleep(random.randint(0,2) * 0.001)
    print('Task %s done' % pid)

def synchronous():
    for i in range(1,10):
        task(i)

async def asynchronous():
    tasks = [asyncio.ensure_future(task_coro(i)) for i in range(1,10)]
    await asyncio.wait(tasks)

print('Synchronous:')
synchronous()


ioloop = asyncio.get_event_loop()
print('Asynchronous')
ioloop.run_until_complete(asynchronous())
ioloop.close()


# you can use the concurrent.futures module to wrap a blocking task in a thread or a process and return a future asyncio can use

