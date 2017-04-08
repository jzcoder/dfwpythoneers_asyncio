"""
Show use of await outside async def

Note: This example intentionally does not work. It is to show that using await outside a native
coroutine is not valid syntax.
"""

import asyncio

async def wait_task(timeout):
    print('STARTING wait_task...')
    asyncio.sleep(timeout)
    print('ENDED')

await wait_task(5)
