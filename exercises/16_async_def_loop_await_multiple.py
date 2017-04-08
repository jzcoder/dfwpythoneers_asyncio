"""
Show multiple concurrent tasks

...
"""
import asyncio
import demo

async def wait_task(timeout, ndx):
    demo.LOG_TASK_START('wait_task', ndx)
    await asyncio.sleep(timeout)
    demo.LOG_TASK_END()

loop = asyncio.get_event_loop()
loop.create_task(wait_task(2, 1))
loop.create_task(wait_task(2, 2))
loop.run_until_complete(wait_task(5, 3))
loop.close()
