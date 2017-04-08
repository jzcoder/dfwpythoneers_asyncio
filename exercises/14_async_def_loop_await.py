"""
Successful async/await event loop

...
"""

import asyncio

async def wait_task():
    print('STARTING wait_task...')
    await asyncio.sleep(5)
    print('ENDED')


loop = asyncio.get_event_loop()
loop.run_until_complete(wait_task())
loop.close()