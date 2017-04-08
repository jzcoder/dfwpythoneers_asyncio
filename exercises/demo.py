"""
This contains some logging utilities for demonstrating multiple async tasks. 
"""
import logging
import time


class ElapsedTimeFormatter():

    def __init__(self):
        self.start_time = time.time()
        self.counter = 0

    def format(self, record):
        elapsed_secs = (record.created - self.start_time)
        self.counter += 1
        return '%04d | %4.2f | %s' % (self.counter, elapsed_secs, record.getMessage())


def init_logger():
    handler = logging.StreamHandler()
    handler.setFormatter(ElapsedTimeFormatter())

    root = logging.getLogger()
    root.addHandler(handler)
    root.setLevel(logging.DEBUG)

init_logger()

LOG = logging.getLogger().info

TASK_MAP = {}
CUR_TASK_ID = 0

def LOG_TASK_START(name, ndx=None):
    LOG(f'Starting: {name}: {task(name, ndx)[0]}')

def LOG_TASK_END():
    task_info = task(None)
    LOG(f'Ending: {task_info[1]}: {task_info[0]}')


def task(name=None, ndx=None):
    from asyncio import Task
    task_id = id(Task.current_task())
    try:
        return TASK_MAP[task_id]
    except KeyError:
        if ndx is None:
            global CUR_TASK_ID
            CUR_TASK_ID += 1
            ndx = CUR_TASK_ID
        TASK_MAP[task_id] = (ndx, name)
        return (ndx, name)
