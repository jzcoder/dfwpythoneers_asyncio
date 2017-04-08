"""
Correctly using executor for a blocking function with thumper

...
"""
import asyncio, demo, time

async def test_timeout():
    demo.LOG_TASK_START('test_timeout')
    await asyncio.get_event_loop().run_in_executor(None, time.sleep, 5)
    demo.LOG_TASK_END()

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
