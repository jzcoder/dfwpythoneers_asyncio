"""
Show result of calling a coroutine function

Note: This example intentionally does not work. Show return type of wait_task() is
a coroutine object.
"""

import asyncio

async def wait_task(timeout):
    print('STARTING wait_task...')
    asyncio.sleep(timeout)
    print('ENDED')

wait_task(5)
