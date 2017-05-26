import asyncio

async def foo():
    print('Running in foo')
    await asyncio.sleep(0) # nonblocking work using the sleep function, await declares that coroutine gives control back to event loop in this case sleep
    # event loop will switch contexts to the next task scheduled for execution
    print('Context switch to foo again')

async def bar():
    print('Explicit context switch to bar')
    await asyncio.sleep(0) #allows the event loop to pass control back to foo
    print('Implicit context switch back to bar')

ioloop = asyncio.get_event_loop()
tasks = [ioloop.create_task(foo()), ioloop.create_task(bar())] # coroutines can only be called from other coroutines or be wrapped in a task and then scheduled
wait_tasks = asyncio.wait(tasks) # combine two tasks into one that waits for both to complete
ioloop.run_until_complete(wait_tasks) #schedule the wait task to run using event loop
ioloop.close()