import time
import asyncio

start = time.time()

def tic():
    return 'at %1.1f seconds' %(time.time() - start)

async def gr1():
    # Busy waits for a second but we dont want to stick around
    print('gr1 started work: {}'.format(tic()))
    await asyncio.sleep(2)
    print('gr1 ended work: {}'.format(tic()))


async def gr2():
    # Busy waits for a second but we dont want to stick around
    print('gr2 started work: {}'.format(tic()))
    await asyncio.sleep(2)
    print('gr2 ended work: {}'.format(tic()))

async def gr3():
    print(' Do stuff while coroutines are blocked, {}'.format(tic()))
    await asyncio.sleep(2)
    print('done')

ioloop = asyncio.get_event_loop()
tasks = [
    ioloop.create_task(gr1()),
    ioloop.create_task(gr2()),
    ioloop.create_task(gr3())
]

ioloop.run_until_complete(asyncio.wait(tasks))
ioloop.close()

# IO loop manages and schedules the execution allwoing single threaded code to operate concurrently
# while two blocking tasks are blocked a third one can control the flow
