""" 
Use a ProcessPoolExecutor instead of default thread pool. 

Note: The overhead compared to thread pool executor. But, it was really easy to switch
to the process pool.
"""
import asyncio, demo, time, os

from concurrent.futures import ProcessPoolExecutor

NUM_TASKS = 20

def blocking_call(timeout, ndx):
    demo.LOG(f"Executing blocking call; ndx={ndx}; pid={os.getpid()}")
    time.sleep(timeout)
    return ndx

async def wait_task(pool, timeout, ndx):
    demo.LOG_TASK_START('wait_task', ndx)
    ndx = await asyncio.get_event_loop().run_in_executor(pool, blocking_call, timeout, ndx)
    demo.LOG_TASK_END()
    return ndx


if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    pool = ProcessPoolExecutor(20)

    cors = [wait_task(pool, 5, i+1) for i in range(0, NUM_TASKS)]

    fut = asyncio.gather(*cors)

    start_time = loop.time()

    result = loop.run_until_complete(fut)
    loop.close()

    demo.LOG(f'result={result}')
