# Provides tools for building concurrent appllications using coroutines
# threading module implements concurrency thourgh application threads
# multiprocessing implements concurrency using system processes
# asyncio uses a single threaded single process approach - parts of an application switch tasks explicitly at optimal times
# most often this context switching occurs hwne the program would otherwise block waiting to read or write data
# also includes support for scheduling code to run at a specific future time

# starting a coroutine

import asyncio

async def coroutine():
    print('in coroutine')

event_loop = asyncio.get_event_loop()#obtain a reference to the event loop
try:
    print('starting coroutine')
    coro = coroutine()
    print('entering event loop')
    event_loop.run_until_complete(coro) # starts the loop with the coroutine object and stops the loop when the coroutine exits by returning
finally:
    print('closing event loop')
    event_loop.close()