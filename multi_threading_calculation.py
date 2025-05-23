import math
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Value, Queue

from find_factors_in_half_interval_with_heuristic import find_factors_in_half_interval

def multi_threading_calculation(number, max_workers):
    value = Value('i', number, lock=True)
    result_queue = Queue()

    chunk_size = (int(number ** 0.5) + max_workers - 1) // max_workers

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = []
        for chunk_ind in range(max_workers):
            futures.append(executor.submit(find_factors_in_half_interval, value, 1 + chunk_ind * chunk_size, 1 + (
                    chunk_ind + 1) * chunk_size, result_queue))
        for future in futures:
            future.result()

    results = []
    while not result_queue.empty():
        results.append(result_queue.get())
    return results

