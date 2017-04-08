"""
Show running 20 tasks works as expected, but what about 21?

Point out that the tasks might not complete in the same order they were created.
However, the results from gather() are in the same order

The executor will default to NUM_CORES * 5 threads.
On this laptop, there are 4 cores.
If we create 20 async tasks, all using run_in_exector, the program finishes in the expected time.
If we create 21 async tasks, we will see one of the tasks will block on the thread pool.
 
Note: This example will behave differently based on the number of cores you have.
"""
import asyncio, demo, time

NUM_TASKS = 20

async def wait_task(ndx, timeout):
    demo.LOG_TASK_START('wait_task', ndx)
    await asyncio.get_event_loop().run_in_executor(None, time.sleep, timeout)
    demo.LOG_TASK_END()
    return ndx

loop = asyncio.get_event_loop()

cors = [wait_task(i+1, 5) for i in range(0, NUM_TASKS)]

fut = asyncio.gather(*cors)
result = loop.run_until_complete(fut)
loop.close()

demo.LOG(f'result={result}')

