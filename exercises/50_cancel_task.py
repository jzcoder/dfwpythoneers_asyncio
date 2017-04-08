""" 
Cancel a running task

Warning --- call_later takes a regular function not a coroutine
"""
import asyncio, demo

async def waiter():
    demo.LOG_TASK_START('waiter')
    try:
        await asyncio.sleep(60)
    except asyncio.CancelledError:
        demo.LOG('** CANCELLED **')
        raise
    demo.LOG_TASK_END()

def stop_writer(task):
    demo.LOG('Cancelling task...')
    task.cancel()

loop = asyncio.get_event_loop()

fut = loop.create_task(waiter())
loop.call_later(5, stop_writer, fut)

loop.run_until_complete(fut)

demo.LOG(f'result={fut.result()}')
