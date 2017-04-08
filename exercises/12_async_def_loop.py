"""
Show default event loop and unexpected behavior

1) Introduce the default event loop
2) Demonstrate sleep does nothing
3) Show return value of sleep() is a generator -- that's why
4) Try yield from and show you can't do that

Note: This example intentionally does not sleep the expected duration.
"""

import asyncio

async def wait_task(timeout):
    print('STARTING wait_task...')
    asyncio.sleep(timeout)
    print('ENDED')

loop = asyncio.get_event_loop()
loop.run_until_complete(wait_task(5))
loop.close()