""" 
How to coordinate producer/consumer tasks
 
NOTE: Show behavior if we don't await on the put operation

Show how we have a fast producer and slow consumer and how asyncio bounded queue
can help.
"""
import asyncio, demo
from random import randint

async def read_data(queue):
    while True:
        await asyncio.sleep(1)
        data = randint(0, 1000)
        demo.LOG(f'adding data to queue... {data}; before queue len={queue.qsize()}')
        await queue.put(data)

async def process_data(queue, ndx):

    while True:
        data = await queue.get()
        demo.LOG(f'processing data [{ndx}]: {data}')
        await asyncio.sleep(5)

loop = asyncio.get_event_loop()
queue = asyncio.Queue(5)
loop.create_task(read_data(queue))
loop.create_task(process_data(queue, 1))

loop.run_forever()
loop.close()
