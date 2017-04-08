""" 
Two independent subtasks are not overlapping

In this example, we would expect the operation to take 4 seconds,
since get_a() can be run concurrently, instead it takes 6 seconds.
this is because we have two separate awaits
"""
import asyncio, demo

async def get_a():
    demo.LOG_TASK_START('get_a')
    await asyncio.sleep(2)
    demo.LOG_TASK_END()
    return 1

async def get_b():
    demo.LOG_TASK_START('get_b')
    await asyncio.sleep(4)
    demo.LOG_TASK_END()
    return 2

async def parent():
    return await get_a() + await get_b()

loop = asyncio.get_event_loop()
result = loop.run_until_complete(parent())
loop.close()
demo.LOG(f'result={result}')