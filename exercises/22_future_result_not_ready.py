""" 
Show what happens using future too early

...
"""
import asyncio, demo

async def get_value(timeout):
    await asyncio.sleep(timeout)
    return 1234

async def compute_value():
    return await get_value(10)

async def wait_task():
    await asyncio.sleep(5)

loop = asyncio.get_event_loop()

calc_task = loop.create_task(compute_value())
wait_task = loop.create_task(wait_task())

loop.run_until_complete(wait_task)

demo.LOG(f'result={calc_task.result()}')
