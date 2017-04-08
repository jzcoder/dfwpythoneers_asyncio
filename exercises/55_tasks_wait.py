"""
Do something after any subordinate task finishes

...
"""
import asyncio, demo
from concurrent.futures import FIRST_COMPLETED

NUM_TASKS = 10

async def wait_task(timeout, ndx):
    demo.LOG_TASK_START(f'wait_task;timeout({timeout})', ndx)
    await asyncio.sleep(timeout)
    demo.LOG_TASK_END()
    return ndx

async def main_task(loop):
    tasks = [loop.create_task(wait_task(i*2, i)) for i in range(1, NUM_TASKS+1)]

    while True:
        demo.LOG('Waiting for any task to finish...')
        done, pending = await asyncio.wait(tasks, loop=loop, return_when=FIRST_COMPLETED)

        for task in done:
            demo.LOG(f'task result: {task.result()}')
            tasks.remove(task)

        if not pending:
            break

    demo.LOG('all subordinate tasks completed; stopping event loop')
    loop.stop()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(main_task(loop))
    loop.run_forever()
    demo.LOG('eventloop terminated')
    loop.close()
