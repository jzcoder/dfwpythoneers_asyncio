""" 
Show Python 3.3 syntax and invalid mixing

...
"""
import asyncio, demo

@asyncio.coroutine
def get_a():
    demo.LOG_TASK_START('get_a')
    yield from asyncio.sleep(2)
    demo.LOG_TASK_END()
    return 1

async def get_b():
    demo.LOG_TASK_START('get_b')
    await asyncio.sleep(4)
    demo.LOG_TASK_END()
    return 2

async def parent():
    result = await asyncio.gather(get_a(), get_b())
    return result[0] + result[1]

loop = asyncio.get_event_loop()

result = loop.run_until_complete(parent())
loop.close()

demo.LOG(f'result={result}')
