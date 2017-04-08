""" 
Show how exceptions are handled from coroutine

...
"""
import asyncio, demo

async def get_value(timeout):
    await asyncio.sleep(timeout)
    demo.LOG('raising get_value error')
    raise Exception('get_value error')

async def compute_value():
    return await get_value(1)

async def wait_task():
    await asyncio.sleep(5)

loop = asyncio.get_event_loop()

calc_task = loop.create_task(compute_value())
wait_task = loop.create_task(wait_task())

loop.run_until_complete(wait_task)

demo.LOG(f'result={calc_task.result()}')
