import asyncio

# asyncio removes around event loop which waits for something to happen and then acts on the event
# responsible for handling such things as I/O and system events
#Once event handlers are done , they need to give control back to event loop, to do this asyncio uses coroutines
# coroutine special function and is a consumer and extension of a generator

async def my_coro():
    await func()


