import asyncio
import math
from asyncio import Queue
from multiprocessing import Value

from find_factors_in_half_interval_with_heuristic_async import find_factors_in_half_interval_async


async def asynchronous_calculation(number, tasks_count):
    value = Value('i', number, lock=True)
    result_queue = Queue()

    chunk_size = (int(number ** 0.5) + tasks_count - 1) // tasks_count
    print(chunk_size)
    tasks = []
    for chunk_ind in range(tasks_count):
        tasks.append(find_factors_in_half_interval_async(value, 1 + chunk_ind * chunk_size, 1 + (chunk_ind + 1) * chunk_size, result_queue))

    await asyncio.gather(*tasks)

    results = []
    while not result_queue.empty():
        results.append(result_queue.get())
    return results
