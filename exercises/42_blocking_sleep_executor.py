"""
Using run_in_executor incorrectly

Note: This example intentionally does not work, because we do not await on the executor future.
"""
import asyncio, demo, time

async def test_timeout():
    asyncio.get_event_loop().run_in_executor(None, time.sleep, 5)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.set_debug(True)

    loop.run_until_complete(test_timeout())
    loop.close()
