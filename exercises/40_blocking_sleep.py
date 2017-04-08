"""
Using a blocking call in coroutine

...
"""
import asyncio, demo, time

async def test_timeout():
    time.sleep(5)

async def thumper():
    while True:
        await asyncio.sleep(1)
        demo.LOG('...thump')

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.set_debug(True)
    loop.create_task(thumper())
    loop.run_until_complete(test_timeout())
    loop.close()
