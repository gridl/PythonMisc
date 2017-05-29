
# start five consumers of the condition, each uses wait() method to wait for a notification that they can proceed
#manipu;ate.condition() notifies one consumer , then two consumers then all the remaining consumers
import asyncio

async def consumer(condition, n):
    with await condition:
        print('consumer {} is waiting'.format(n))
        await condition.wait()
        print('conumser {} triggered'.format(n))
    print('ending consumer {}'.format(n))

async def manipulate_condition(condition):
    print('Starting manipulate_condition')

    # pause to let consumers start
    await asyncio.sleep(0.1)

    for i in range(1,3):
        with await condition:
            print('notifying {} consumers'.format(i))
            condition.notify(n=i)
        await asyncio.sleep(0.1)

    with await condition:
        print('notifying remaining consumers')
        condition.notify_all()

    print('ending manoulate_condition')

async def main(loop):
    # create a condition
    condition = asyncio.Condition()

    #set up tasks watching the condition
    consumers = [ consumer(condition,i) for i in range(5)]

    #schedule a taks to manipulate the condition variable
    loop.create_task(manipulate_condition(condition))

    # wait for consumers to be done
    await asyncio.wait(consumers)

event_loop = asyncio.get_event_loop()
try:
    result = event_loop.run_until_complete(main(event_loop))
finally:
    event_loop.close()

