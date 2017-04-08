""" 
Explicitly ending the event loop from a task

...
"""
import asyncio, demo

async def waiter():
    demo.LOG_TASK_START('waiter')
    try:
        await asyncio.sleep(60)
    except asyncio.CancelledError:
        demo.LOG('waiter **CANCELLED**')

async def stop_task():
    await asyncio.sleep(10)

    demo.LOG('Stopping event loop...')
    loop = asyncio.get_event_loop()
    loop.stop()


loop = asyncio.get_event_loop()
loop.create_task(stop_task())
loop.create_task(waiter())

demo.LOG('Starting event loop forever...')
loop.run_forever()
demo.LOG("Event loop terminated")
loop.close()